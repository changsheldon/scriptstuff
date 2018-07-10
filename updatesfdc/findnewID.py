import SFLogin
import BQlogin
import Appnexuslogin
import csv

def findnewID():
#BQdata = {}

	SFDCdata = SFLogin.salesforcedata()
	BQdata = BQlogin.BQdata()
	AppnexusData = Appnexuslogin.AppnexusData()
	LiveID = {}
	changedarray = {}
	errorarray = {}

	with open('LiveRampIDs.csv', 'rU') as LiveRampID_file:
		LiveRampIDs = csv.DictReader(LiveRampID_file)

		for Segname in LiveRampIDs:
			LiveID.update({Segname['Segment Name']: Segname['LiveRamp Segment ID']})
		LiveRampID_file.close()

		with open('updated_SFDC.csv', 'w') as newSFDC_file:
			newheader = ['IDs', 'Product Date','Opportunity Owner', 'Agency Holding Company', 'Account Name', 'Opportunity Name',  'LineItemID','Segment Name','Endpoint']
			SFDC_writer = csv.writer(newSFDC_file, delimiter=',')

			for LineItemID in SFDCdata:
				if LineItemID =='':
					pass
				else:
					if SFDCdata[LineItemID]['Segment ID'] != 'None' or SFDCdata[LineItemID]['Segment ID'] != '-' or  SFDCdata[LineItemID]['Segment ID'] != '':
						if SFDCdata[LineItemID]['Endpoint'] == 'TTD':
							#print(SFDCdata[LineItemID]['Segment ID'])
							try:
								SFDCdata[LineItemID]['Segment ID'] = BQdata[0][SFDCdata[LineItemID]['Segment Name']]['ID']
							except KeyError as e:
								print('KeyError: Segment not found in TTD file')
								print(e)
								errorarray[LineItemID] = SFDCdata[LineItemID]
							else:
								pass
							
							#print(SFDCdata[LineItemID]['Segment ID'])
							#print('ID for TTD changed')
							changedarray[LineItemID] = SFDCdata[LineItemID]
						elif SFDCdata[LineItemID]['Endpoint'] == 'Eyeota':
							#print(SFDCdata[LineItemID]['Segment ID'])
							try:
								SFDCdata[LineItemID]['Segment ID'] = BQdata[1][SFDCdata[LineItemID]['Segment Name']]['ID']
							except KeyError as e:
								print('KeyError: Segment not found in Eyeota file')
								print(e)
								errorarray[LineItemID] = SFDCdata[LineItemID]
							else:
								pass
							
							#print(SFDCdata[LineItemID]['Segment ID'])
							#print('ID for Eyeota changed')
							changedarray[LineItemID] = SFDCdata[LineItemID]
						elif SFDCdata[LineItemID]['Endpoint'] == 'Appnexus':
							#print(SFDCdata[LineItemID]['Segment ID'])
							try:
								SFDCdata[LineItemID]['Segment ID'] = AppnexusData[SFDCdata[LineItemID]['Segment Name']]
							except KeyError as e:
								print('KeyError: Segment not found in Appnexus File')
								print(e)
								errorarray[LineItemID] = SFDCdata[LineItemID]
							else:
								pass
							
							#print(SFDCdata[LineItemID]['Segment ID'])
							#print('ID for Appnexus changed')
							changedarray[LineItemID] = SFDCdata[LineItemID]
						elif SFDCdata[LineItemID]['Endpoint'] == 'LiveRamp':
							#print(SFDCdata[LineItemID]['Segment ID'])
							#print(LiveID[SFDCdata[LineItemID]['Segment Name']])
							try:
								SFDCdata[LineItemID]['Segment ID'] = LiveID[SFDCdata[LineItemID]['Segment Name']]
							except KeyError as e:
								print('KeyError: Segment not found in LiveRamp file')
								print(e)
								errorarray[LineItemID] = SFDCdata[LineItemID]
							else:
								pass
								#SFDCdata[LineItemID]['Segment ID'] = LiveID[SFDCdata[LineItemID]['Segment Name']]['LiveRamp Segment ID']
								
								#print(SFDCdata[LineItemID]['Segment ID'])
								#print('ID for LiveRamp changed')
								changedarray[LineItemID] = SFDCdata[LineItemID]
					else:
						#print('nothing')
						pass
			#print(changedarray)
			SFDC_writer.writerow(newheader)
			for newline in SFDCdata:
						#print newline
				SFDC_writer.writerow([SFDCdata[newline]['Segment ID'], SFDCdata[newline]['Product Date'],SFDCdata[newline]['Opportunity Owner'],SFDCdata[newline]['Agency Holding Company'],SFDCdata[newline]['Account Name'],SFDCdata[newline]['Opportunity Name'],newline,SFDCdata[newline]['Segment Name'],SFDCdata[newline]['Endpoint']])
			newSFDC_file.close()

		with open('changed_SFDC.csv', 'w') as changedSFDC_file:
			newheader = ['IDs', 'Product Date','Opportunity Owner', 'Agency Holding Company', 'Account Name', 'Opportunity Name',  'LineItemID','Segment Name','Endpoint']
			changed_writer = csv.writer(changedSFDC_file, delimiter=',')
			changed_writer.writerow(newheader)
			for stuff in changedarray:
				#print newline
				changed_writer.writerow([changedarray[stuff]['Segment ID'], changedarray[stuff]['Product Date'],changedarray[stuff]['Opportunity Owner'],changedarray[stuff]['Agency Holding Company'],changedarray[stuff]['Account Name'],changedarray[stuff]['Opportunity Name'],stuff,changedarray[stuff]['Segment Name'],changedarray[stuff]['Endpoint']])
			changedSFDC_file.close()
		#print(changedarray)
		with open('error_SFDC.csv', 'w') as errorSFDC_file:
			newheader = ['IDs', 'Product Date','Opportunity Owner', 'Agency Holding Company', 'Account Name', 'Opportunity Name',  'LineItemID','Segment Name','Endpoint']
			error_writer = csv.writer(errorSFDC_file, delimiter=',')
			error_writer.writerow(newheader)
			for stuff in errorarray:
				#print newline
				error_writer.writerow([errorarray[stuff]['Segment ID'], errorarray[stuff]['Product Date'],errorarray[stuff]['Opportunity Owner'],errorarray[stuff]['Agency Holding Company'],errorarray[stuff]['Account Name'],errorarray[stuff]['Opportunity Name'],stuff,errorarray[stuff]['Segment Name'],errorarray[stuff]['Endpoint']])
			errorSFDC_file.close()
		#print(errorarray)	
	print('Find new IDs was successful')