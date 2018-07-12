from formatscripts import findnewID
from formatscripts import DSsegments
from formatscripts import format
import csv
import time
import os

def formatusage(hardcodeUpdateInput,thepath,reportinginput,MonthInput,YearInput):
	SFDC = {}
	DSsegmentsData = []
	path2 = '/Users/sheldonchang/Desktop/scriptstuff/UsageApp/app/uploadfile/'
	#make sure all data is updated
	UpdateInputcheck = 'not valid'

	while UpdateInputcheck != 'valid':
		
		UpdateInput = hardcodeUpdateInput
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
		DSsegmentsreader = csv.reader(DSsegments_file)

		for line in DSsegmentsreader:
			DSsegmentsData.append(line[0])
		DSsegments_file.close()

	print('Got DSsegments data')
	#-----------------------------------end DSsegments data file------------------------------------	

	#open Salesforce data file	
	with open(os.path.join(path2,'Updated_SFDC.csv'), 'rU', encoding='ISO-8859-1') as salesforce_file:
		salesforcedata = csv.DictReader(salesforce_file)

		for line in salesforcedata:
			
	#put the data into a dictionary by Segment ID to remove the duplicates and get the opp with the latest date
			if line['IDs'] not in SFDC:
				SFDC[line['IDs']] = {'Product Date' : line['Product Date'], 'Opportunity Owner': line['Opportunity Owner'], 'Agency Holding Company': line['Agency Holding Company'], 'Opportunity Name': line['Opportunity Name'], 'LineItemID': line['LineItemID'], 'Segment Name':line['Segment Name'], 'Endpoint': line['Endpoint'], 'Account Name': line['Account Name']}
			else:
				if line['Product Date'] == '':
					pass
				else:
					if SFDC[line['IDs']]['Product Date'] == '':
						SFDC[line['IDs']] = {'Product Date' : line['Product Date'], 'Opportunity Owner': line['Opportunity Owner'], 'Agency Holding Company': line['Agency Holding Company'], 'Opportunity Name': line['Opportunity Name'], 'LineItemID': line['LineItemID'], 'Segment Name':line['Segment Name'], 'Endpoint': line['Endpoint'], 'Account Name': line['Account Name']}
					else:
						if line['IDs'] == '-' or line['IDs'] =='':
							pass
						else:
							linedate = time.strptime(line['Product Date'], "%Y-%m-%d")
							SFDCdate = time.strptime(SFDC[line['IDs']]['Product Date'], "%Y-%m-%d")

							if SFDCdate < linedate:
								#print(line['ID'],SFDC[line['ID']])
								#print('Duplicate Segment ID')
								SFDC[line['IDs']] = {'Product Date' : line['Product Date'], 'Opportunity Owner': line['Opportunity Owner'], 'Agency Holding Company': line['Agency Holding Company'], 'Opportunity Name': line['Opportunity Name'], 'LineItemID': line['LineItemID'], 'Segment Name':line['Segment Name'], 'Endpoint': line['Endpoint'], 'Account Name': line['Account Name']}
								#print(line['ID'],SFDC[line['ID']])
							else:
								pass

		salesforce_file.close()
	print('Got SFDC data')


	print('Starting formatting')
	format.format(reportinginput,MonthInput,YearInput,SFDC,DSsegmentsData,thepath)

	print('Finished!')
