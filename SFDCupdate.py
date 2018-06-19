import csv
import time
#import json

SFDC = {}
UpdateSFDCdata = {}
liveIDdict = {}
ttdIDdict = {}
eyeotaIDdict = {}
appnexusIDdict = {}
otherIDdict = {}

#SFDC = {'IDs': {'Opportunity Owner': 'Opportunity Owner', 'Agency Holding Company':'Agency Holding Company', 'Account Name':'Account Name','Opportunity Name': 'Opportunity Name', 'Product Date': 'Product Date', 'LineItemID': 'LineItemID', 'Segment Name': 'Segment Name', 'Endpoint': 'Endpoint'}}

#print SFDC
#UpdateSFDCdata = {'LineItemID': {'Opportunity Owner': 'Opportunity Owner', 'Agency Holding Company':'Agency Holding Company', 'Account Name':'Account Name','Opportunity Name': 'Opportunity Name', 'Product Date': 'Product Date', 'Segment Name': 'Segment Name', 'Endpoint': 'Endpoint'}}
IDkeys = []
SFDCkeys = []
#liveIDdict = {'Segment Name': 'Segment Name', 'ID': 'ID'}
#ttdIDdict = {'name': 'ID'}
#eyeotaIDdict = {'name': 'ID'}
#appnexusIDdict = {'name': 'ID'}
#otherIDdict = {'destination_seg_id': 'ID', 'name': 'Segment Name', 'destination_name':'Endpoint'}

with open('SFDCtest.csv', 'rU') as csv_file:
	SFDC_reader = csv.DictReader(csv_file)
	i=1
	for line in SFDC_reader:
		if line.get('IDs') != '-':
			if line.get('IDs') not in IDkeys:
				SFDC.update({line.get('IDs'): {'LineItemID': line.get('LineItemID'), 'data' :{'Opportunity Owner': line.get('Opportunity Owner'), 'Agency Holding Company':line.get('Agency Holding Company'), 'Account Name':line.get('Account Name'),'Opportunity Name': line.get('Opportunity Name'), 'Product Date': line.get('Product Date'), 'Segment Name': line.get('Segment Name'), 'Endpoint': line.get('Endpoint')}}})
				SFDCkeys.append(line.get('LineItemID'))
				IDkeys.append(line.get('IDs'))
			else:
				print 'duplicate found'
				print line
				if SFDC[line.get('IDs')]['data']['Product Date'] == '':
					SFDC[line.get('IDs')]['LineItemID'] = line.get('LineItemID')
					SFDC[line.get('IDs')]['data'] = {'Opportunity Owner': line.get('Opportunity Owner'), 'Agency Holding Company':line.get('Agency Holding Company'), 'Account Name':line.get('Account Name'),'Opportunity Name': line.get('Opportunity Name'), 'Product Date': line.get('Product Date'),  'Segment Name': line.get('Segment Name'), 'Endpoint': line.get('Endpoint')}

				else:
 					newdate1 = time.strptime(line.get('Product Date'), "%m/%d/%y")
 					newdate2 = time.strptime(SFDC[line.get('IDs')]['data']['Product Date'], "%m/%d/%y")

 					if newdate1 > newdate2:
	 					print 'there was a change'

 						SFDC[line.get('IDs')]['LineItemID'] = line.get('LineItemID')
						SFDC[line.get('IDs')]['data'] = {'Opportunity Owner': line.get('Opportunity Owner'), 'Agency Holding Company':line.get('Agency Holding Company'), 'Account Name':line.get('Account Name'),'Opportunity Name': line.get('Opportunity Name'), 'Product Date': line.get('Product Date'),  'Segment Name': line.get('Segment Name'), 'Endpoint': line.get('Endpoint')}

 					else:
 						pass


# 				if SFDC[line.get('IDs')]['Product Date'] == '':
# 					pass	
# 				else:
# 					newdate1 = time.strptime(line.get('Product Date'), "%m/%d/%y")
# 					newdate2 = time.strptime(SFDC[line.get('IDs')]['Product Date'], "%m/%d/%y")

# 				#print SFDC[line.get('IDs')]['Product Date']
# 					if newdate1 > newdate2:
# 					#print 'there was a change'

# 						SFDC[line.get('IDs')] = {'Opportunity Owner': line.get('Opportunity Owner'), 'Agency Holding Company':line.get('Agency Holding Company'), 'Account Name':line.get('Account Name'),'Opportunity Name': line.get('Opportunity Name'), 'Product Date': line.get('Product Date'), 'LineItemID': line.get('LineItemID'), 'Segment Name': line.get('Segment Name'), 'Endpoint': line.get('Endpoint')}
# 					else:
# 						pass



			# IDkeys.append(line.get('IDs'))
			# SFDC.update({line.get('IDs'): {'LineItemID': line.get('LineItemID'), 'data' :{'Opportunity Owner': line.get('Opportunity Owner'), 'Agency Holding Company':line.get('Agency Holding Company'), 'Account Name':line.get('Account Name'),'Opportunity Name': line.get('Opportunity Name'), 'Product Date': line.get('Product Date'), 'Segment Name': line.get('Segment Name'), 'Endpoint': line.get('Endpoint')}}})
			# SFDCkeys.append(line.get('LineItemID'))

		 	

	with open('new_testSFDC.csv', 'w') as csv_file:
		newheader = ['ID', 'Product Date','Opportunity Owner', 'Agency Holding Company', 'Account Name', 'Opportunity Name',  'LineItemID','Segment Name','Endpoint']
		csv_writer = csv.writer(csv_file, delimiter=',')


			
		with open('UpdateSFDC.csv', 'rU') as csv_file:
			UpdateSFDC = csv.DictReader(csv_file)
			i = 1
			for UpdateSFDCline in UpdateSFDC:
				#print UpdateSFDCline['LineItemID']
				if UpdateSFDCline['LineItemID'] == '':
					pass
				else:
					UpdateSFDCdata[UpdateSFDCline.get('LineItemID')] = {'Opportunity Owner': UpdateSFDCline.get('Opportunity Owner'), 'Agency Holding Company':UpdateSFDCline.get('Agency Holding Company'), 'Account Name':UpdateSFDCline.get('Account Name'),'Opportunity Name': UpdateSFDCline.get('Opportunity Name'), 'Product Date': UpdateSFDCline.get('Product Date'), 'Segment Name': UpdateSFDCline.get('Segment Name'), 'Endpoint': UpdateSFDCline.get('Endpoint')}
					if UpdateSFDCline['LineItemID'] not in SFDCkeys:
						tempID = 'new' + str(i)
						SFDC.update({tempID : {'LineItemID': UpdateSFDCline.get('LineItemID'), 'data' : UpdateSFDCline}})
						i += 1
						#print 'there was a new entry'
						#print line
					#UpdateSFDCdata[line.get('LineItemID')] = {'Opportunity Owner': line.get('Opportunity Owner'), 'Agency Holding Company':line.get('Agency Holding Company'), 'Account Name':line.get('Account Name'),'Opportunity Name': line.get('Opportunity Name'), 'Product Date': line.get('Product Date')}
			
# 	#--------------------------------------------get IDs for each end point------------------------------------
		with open('LiveRampIDs.csv', 'rU') as csv_file:
			LiveRampIDs = csv.DictReader(csv_file)

			for Segname in LiveRampIDs:
				liveIDdict.update({Segname['Segment Name']: Segname['LiveRamp Segment ID']})

		with open('BQID.csv', 'rU') as csv_file:
			BQIDs = csv.DictReader(csv_file)

			for Segname in BQIDs:
				if Segname['destination_name'] == 'ttd':
					ttdIDdict.update({Segname['name']: Segname['destination_seg_id']})
				elif Segname['destination_name'] == 'eyeota':
					eyeotaIDdict.update({Segname['name']: Segname['destination_seg_id']})
				elif Segname['destination_name'] == 'appnexus':
					appnexusIDdict.update({Segname['name']: Segname['destination_seg_id']})
				else:
					pass
					#print Segname
					#otherIDdict.update({'destination_seg_id': Segname['destination_seg_id'], 'name': Segname['name'], 'destination_name':Segname['destination_name']})


# #--------------------------------------------END get IDs for each end point------------------------------------


			for line in SFDC:
				if SFDC[line]['LineItemID'] == '':
					pass
				else:
					SFDC[line]['data'] = UpdateSFDCdata[SFDC[line]['LineItemID']]

				#based on data in UpdateSFDCdata
				if line.find('new') > -1 or line == '' or line == '-':

					if SFDC[line]['data']['Endpoint'] == 'TTD':

						segmentnamevalue = SFDC[line]['data']['Segment Name']
						if segmentnamevalue not in ttdIDdict or segmentnamevalue =='':
							pass
						else:
							print 'found new TTD ID'
							SFDC[ttdIDdict[segmentnamevalue]] = SFDC.pop(line)
					elif SFDC[line]['data']['Endpoint'] == 'LiveRamp':

						segmentnamevalue = SFDC[line]['data']['Segment Name']
						if segmentnamevalue not in liveIDdict or segmentnamevalue =='':
							pass
						else:
							print 'found new LiveRamp ID'
							SFDC[liveIDdict[segmentnamevalue]] = SFDC.pop(line)

					elif SFDC[line]['data']['Endpoint'] == 'Eyeota':
						segmentnamevalue = SFDC[line]['data']['Segment Name']
						if segmentnamevalue not in eyeotaIDdict or segmentnamevalue =='':
							pass
						else:
							print 'found new Eyeota ID'
							SFDC[eyeotaIDdict[segmentnamevalue]] = SFDC.pop(line)

					elif SFDC[line]['data']['Endpoint'] == 'Appnexus':

						segmentnamevalue = SFDC[line]['data']['Segment Name']
						if segmentnamevalue not in appnexusIDdict or segmentnamevalue =='':
							pass
						else:
							print 'found new Appnexus ID'
							SFDC[appnexusIDdict[segmentnamevalue]] = SFDC.pop(line)

					else:
						#Endpoint value in SFDC is blank or = '-'
						pass

# #write final update to new file
				
			csv_writer.writerow(newheader)
			for newline in SFDC:
				print newline
				csv_writer.writerow([newline,SFDC[newline]['data']['Product Date'],SFDC[newline]['data']['Opportunity Owner'],SFDC[newline]['data']['Agency Holding Company'],SFDC[newline]['data']['Account Name'],SFDC[newline]['data']['Opportunity Name'],SFDC[newline]['LineItemID'],SFDC[newline]['data']['Segment Name'],SFDC[newline]['data']['Endpoint']])

			print 'done'

				#if line not in newIDkey:
				#	newIDkey.append(line)
				#print SFDC[line]
				#SFDC[line.get('IDs')][line.get('LineItemID')] = UpdateSFDCdata[line.get('LineItemID')]
				#else:
				#	blah = SFDC[line]
						#print blah
					#if SFDC[line]['Product Date'] == '':
# 			else:
# 				if SFDC[line.get('IDs')]['Product Date'] == '':
# 					pass	
# 				else:
# 					newdate1 = time.strptime(line.get('Product Date'), "%m/%d/%y")
# 					newdate2 = time.strptime(SFDC[line.get('IDs')]['Product Date'], "%m/%d/%y")

# 				#print SFDC[line.get('IDs')]['Product Date']
# 					if newdate1 > newdate2:
# 					#print 'there was a change'

# 						SFDC[line.get('IDs')] = {'Opportunity Owner': line.get('Opportunity Owner'), 'Agency Holding Company':line.get('Agency Holding Company'), 'Account Name':line.get('Account Name'),'Opportunity Name': line.get('Opportunity Name'), 'Product Date': line.get('Product Date'), 'LineItemID': line.get('LineItemID'), 'Segment Name': line.get('Segment Name'), 'Endpoint': line.get('Endpoint')}
# 					else:
# 						pass
# 			#print line
# 			# if line.get('IDs') != '-':
# 			# 	SFDC.update({line.get('IDs'): {'Opportunity Owner': line.get('Opportunity Owner'), 'Agency Holding Company':line.get('Agency Holding Company'), 'Account Name':line.get('Account Name'),'Opportunity Name': line.get('Opportunity Name'), 'Product Date': line.get('Product Date'), 'LineItemID': line.get('LineItemID'), 'Segment Name': line.get('Segment Name'), 'Endpoint': line.get('Endpoint')}})
# 			# 	SFDCkeys.append(line.get('LineItemID'))
# 			# 	IDkeys.append(line.get('IDs'))
		
# 		#for line in SFDC_reader:

# 			if line.get('LineItemID') not in IDkeys:
# 				IDkeys.append(line.get('IDs'))
# 				SFDC[line.get('IDs')] = {'Opportunity Owner': line.get('Opportunity Owner'), 'Agency Holding Company':line.get('Agency Holding Company'), 'Account Name':line.get('Account Name'),'Opportunity Name': line.get('Opportunity Name'), 'Product Date': line.get('Product Date'), 'LineItemID': line.get('LineItemID'), 'Segment Name': line.get('Segment Name'), 'Endpoint': line.get('Endpoint')}

# 			else:
# 				if SFDC[line.get('IDs')]['Product Date'] == '':
# 					pass	
# 				else:
# 					newdate1 = time.strptime(line.get('Product Date'), "%m/%d/%y")
# 					newdate2 = time.strptime(SFDC[line.get('IDs')]['Product Date'], "%m/%d/%y")

# 				#print SFDC[line.get('IDs')]['Product Date']
# 					if newdate1 > newdate2:
# 					#print 'there was a change'

# 						SFDC[line.get('IDs')] = {'Opportunity Owner': line.get('Opportunity Owner'), 'Agency Holding Company':line.get('Agency Holding Company'), 'Account Name':line.get('Account Name'),'Opportunity Name': line.get('Opportunity Name'), 'Product Date': line.get('Product Date'), 'LineItemID': line.get('LineItemID'), 'Segment Name': line.get('Segment Name'), 'Endpoint': line.get('Endpoint')}
# 					else:
# 						pass
# 		#print SFDC	

# 	#--------------------------------------------get IDs for each end point------------------------------------
# 		with open('LiveRampIDs.csv', 'rU') as csv_file:
# 			LiveRampIDs = csv.DictReader(csv_file)

# 			for Segname in LiveRampIDs:
# 				liveIDdict.update({Segname['Segment Name']: Segname['LiveRamp Segment ID']})

# 			with open('BQID.csv', 'rU') as csv_file:
# 				BQIDs = csv.DictReader(csv_file)

# 				for Segname in BQIDs:
# 					if Segname['destination_name'] == 'ttd':
# 						ttdIDdict.update({Segname['name']: Segname['destination_seg_id']})
# 					elif Segname['destination_name'] == 'eyeota':
# 						eyeotaIDdict.update({Segname['name']: Segname['destination_seg_id']})
# 					elif Segname['destination_name'] == 'appnexus':
# 						appnexusIDdict.update({Segname['name']: Segname['destination_seg_id']})
# 					else:
# 						pass
# 						#print Segname
# 						#otherIDdict.update({'destination_seg_id': Segname['destination_seg_id'], 'name': Segname['name'], 'destination_name':Segname['destination_name']})


# #--------------------------------------------END get IDs for each end point------------------------------------
# #--------------------------------------------Update SFDC and find new seg IDs------------------------------------
# 				for thing in SFDC:
					
# 					if SFDC[thing]['LineItemID'] == '':
# 						pass
# 					else:
# 						SFDC[thing]['Opportunity Owner'] = UpdateSFDCdata[SFDC[thing]['LineItemID']]['Opportunity Owner']
# 						SFDC[thing]['Opportunity Name'] = UpdateSFDCdata[SFDC[thing]['LineItemID']]['Opportunity Name']
# 						SFDC[thing]['Account Name'] = UpdateSFDCdata[SFDC[thing]['LineItemID']]['Account Name']
# 						SFDC[thing]['Agency Holding Company'] = UpdateSFDCdata[SFDC[thing]['LineItemID']]['Agency Holding Company']
# 						SFDC[thing]['Product Date'] = UpdateSFDCdata[SFDC[thing]['LineItemID']]['Product Date']
# 						SFDC[thing]['Segment Name'] = UpdateSFDCdata[SFDC[thing]['LineItemID']]['Segment Name']
# 						SFDC[thing]['Endpoint'] = UpdateSFDCdata[SFDC[thing]['LineItemID']]['Endpoint']

# 					if thing == '-' or thing =='':
# 						if SFDC[thing]['Endpoint'] == 'TTD':

# 							segmentnamevalue = SFDC[thing]['Segment Name']
# 							if segmentnamevalue not in ttdIDdict or segmentnamevalue =='':
# 								pass
# 							else:
# 								print 'found new TTD ID'
# 								SFDC[ttdIDdict[segmentnamevalue]] = SFDC.pop(thing)
# 						elif SFDC[thing]['Endpoint'] == 'LiveRamp':

# 							segmentnamevalue = SFDC[thing]['Segment Name']
# 							if segmentnamevalue not in liveIDdict or segmentnamevalue =='':
# 								pass
# 							else:
# 								print 'found new LiveRamp ID'
# 								SFDC[liveIDdict[segmentnamevalue]] = SFDC.pop(thing)

# 						elif SFDC[thing]['Endpoint'] == 'Eyeota':
# 							segmentnamevalue = SFDC[thing]['Segment Name']
# 							if segmentnamevalue not in eyeotaIDdict or segmentnamevalue =='':
# 								pass
# 							else:
# 								print 'found new Eyeota ID'
# 								SFDC[eyeotaIDdict[segmentnamevalue]] = SFDC.pop(thing)

# 						elif SFDC[thing]['Endpoint'] == 'Appnexus':

# 							segmentnamevalue = SFDC[thing]['Segment Name']
# 							if segmentnamevalue not in appnexusIDdict or segmentnamevalue =='':
# 								pass
# 							else:
# 								print 'found new Appnexus ID'
# 								SFDC[appnexusIDdict[segmentnamevalue]] = SFDC.pop(thing)

# 						else:
# 							#Endpoint value in SFDC is blank or = '-'
# 							pass

# #--------------------------------------------End Update SFDC and find new seg IDs------------------------------------
# #write final update to new file
				
# 				csv_writer.writerow(newheader)
# 				for newline in SFDC:
# 					csv_writer.writerow([newline,SFDC[thing]['Product Date'],SFDC[thing]['Opportunity Owner'],SFDC[thing]['Agency Holding Company'],SFDC[thing]['Account Name'],SFDC[thing]['Opportunity Name'],SFDC[thing]['LineItemID'],SFDC[thing]['Segment Name'],SFDC[thing]['Endpoint']])

# print 'done'
