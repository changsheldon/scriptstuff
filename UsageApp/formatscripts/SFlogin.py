from simple_salesforce import Salesforce
#import pandas as pd

def salesforcedata():
	sf = Salesforce(username='sheldon@sharethis.com', password='Shoh6Use', security_token='7H8CqwN6IXwkvEycMGTZkMl4')

	Data = sf.query_all("SELECT Id,OpportunityLineItem.Segment_Name__c,OpportunityLineItem.segment_ID__c,OpportunityLineItem.EndPoint__c,Opportunity.Name,Opportunity.Owner.Name,Opportunity.Account.Name, Opportunity.Agency_Holding_Company__c, ServiceDate FROM OpportunityLineItem Where PriceBookEntry.Name = '*Segment Building'")


	Data2 = Data['records']

	SFDCrecords = {}



	for dictionary in Data2:
		for thing in dictionary:
			
			if dictionary['Id'] in SFDCrecords:
				# print('There are duplicates')
				# duplicate = [dictionary['Segment_Name__c'], dictionary['segment_ID__c'], dictionary['Opportunity']['Name'],dictionary['ServiceDate']]
				# print(duplicate)
				# print(newrecords[dictionary['Id']])
				# UsageReportInput = input('Input Pause')
				pass
			else:
				#lala.append(dictionary['Id'])
				SFDCrecords[dictionary['Id']] = {'Segment Name' : dictionary['Segment_Name__c'], 'Segment ID' : dictionary['segment_ID__c'], 'Endpoint' :dictionary['EndPoint__c'], 'Opportunity Name': dictionary['Opportunity']['Name'], 'Opportunity Owner': dictionary['Opportunity']['Owner']['Name'], 'Account Name': dictionary['Opportunity']['Account']['Name'],'Agency Holding Company': dictionary['Opportunity']['Agency_Holding_Company__c'],'Product Date' : dictionary['ServiceDate']}
	print('SF login was successful')
	return SFDCrecords
	