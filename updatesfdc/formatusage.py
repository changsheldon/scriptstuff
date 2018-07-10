import findnewID
import DSsegments
import format
import csv
import time

SFDC = {}
DSsegmentsData = []

#make sure all data is updated
UpdateInputcheck = 'not valid'

while UpdateInputcheck != 'valid':
	
	UpdateInput = input('Do you want to update SFDC? y/n: ')
	if UpdateInput == 'y' or UpdateInput =='n':
		UpdateInputcheck = 'valid'
	#elif UpdateInput == '':
	#	UpdateInputcheck = 'not valid'
	else:
		UpdateInputcheck = 'not valid'
		print('Please input y/n: ')


#----------------------------------------update SFDC section--------------------------------
if UpdateInput == 'y':
	findnewID.findnewID()
	DSsegments.DSsegments()
	print('Update of SFDC and DS segments was successful')

#----------------------------------------end update section--------------------------------

#open DSsegments data file	
with open('DSsegments.csv', 'rU', encoding='ISO-8859-1') as DSsegments_file:
	DSsegments = csv.reader(DSsegments_file)

	for line in DSsegments:
		DSsegmentsData.append(line[0])
	DSsegments_file.close()

print('Got DSsegments data')
#-----------------------------------end DSsegments data file------------------------------------	

#open Salesforce data file	
with open('Updated_SFDC.csv', 'rU', encoding='ISO-8859-1') as salesforce_file:
	salesforcedata = csv.DictReader(salesforce_file)

	for line in salesforcedata:
		
#put the data into a dictionary by Segment ID to remove the duplicates and get the opp with the latest date
		if line['ID'] not in SFDC:
			SFDC[line['ID']] = {'Product Date' : line['Product Date'], 'Opportunity Owner': line['Opportunity Owner'], 'Agency Holding Company': line['Agency Holding Company'], 'Opportunity Name': line['Opportunity Name'], 'LineItemID': line['LineItemID'], 'Segment Name':line['Segment Name'], 'Endpoint': line['Endpoint'], 'Account Name': line['Account Name']}
		else:
			if line['Product Date'] == '':
				pass
			else:
				if SFDC[line['ID']]['Product Date'] == '':
					SFDC[line['ID']] = {'Product Date' : line['Product Date'], 'Opportunity Owner': line['Opportunity Owner'], 'Agency Holding Company': line['Agency Holding Company'], 'Opportunity Name': line['Opportunity Name'], 'LineItemID': line['LineItemID'], 'Segment Name':line['Segment Name'], 'Endpoint': line['Endpoint'], 'Account Name': line['Account Name']}
				else:
					if line['ID'] == '-' or line['ID'] =='':
						pass
					else:
						linedate = time.strptime(line['Product Date'], "%Y-%m-%d")
						SFDCdate = time.strptime(SFDC[line['ID']]['Product Date'], "%Y-%m-%d")

						if SFDCdate < linedate:
							#print(line['ID'],SFDC[line['ID']])
							#print('Duplicate Segment ID')
							SFDC[line['ID']] = {'Product Date' : line['Product Date'], 'Opportunity Owner': line['Opportunity Owner'], 'Agency Holding Company': line['Agency Holding Company'], 'Opportunity Name': line['Opportunity Name'], 'LineItemID': line['LineItemID'], 'Segment Name':line['Segment Name'], 'Endpoint': line['Endpoint'], 'Account Name': line['Account Name']}
							#print(line['ID'],SFDC[line['ID']])
						else:
							pass

	salesforce_file.close()
print('Got SFDC data')


reportinginput = 'false'



while reportinginput == 'false':
	ReportDict = ["Nielsen", "Eyeota Branded", "Eyeota Whitelabel", "LiveRamp", "TTD", "Lotame", "Appnexus"]
	UsageReportInput = input('Enter Usage report you are trying to format: ')

	for value in ReportDict:
		if UsageReportInput == value:
			reportinginput = 'true'
		else:
			pass
			
	if reportinginput == 'false':
		print('Please Enter a valid report: Nielsen or Eyeota Branded or Eyeota Whitelabel or LiveRamp or TTD or Lotame')

MonthInput = input('What is the month of the Usage Report? ')
YearInput = input('Year? ')

print('Starting formatting')
format.format(UsageReportInput,MonthInput,YearInput,SFDC,DSsegmentsData)

print('Finished!')
