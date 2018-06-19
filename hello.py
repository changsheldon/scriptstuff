import csv

UsageReportInput = raw_input('Enter Usage report you are trying to format: ')
MonthInput = raw_input('What is the month of the Usage Report? ')
YearInput = raw_input('Year? ')
ReportDict = ["Nielsen", "Eyeota Branded", "Eyeota Whitelabel", "LiveRamp", "TTD", "Lotame", "Appnexus"]


UsageReportInputCheck = 'check'

	#checks if input is a valid input
for dictvalue in ReportDict:
	if dictvalue == UsageReportInput:
		print UsageReportInput, dictvalue
		UsageReportInputCheck = 'Valid'

	#checks if input is blank. If not blank then not valid
if not UsageReportInput and not UsageReportInput.strip():
	print 'Please Enter a valid report.'
	quit()
elif UsageReportInputCheck == 'check':
	print 'Please Enter a valid report: Nielsen or Eyeota Branded or Eyeota Whitelabel or LiveRamp or TTD or Lotame'


#WhitelabelDS section------------------------------------------------------------------------------------
whitelabeldssegments = []

with open('whitelabelds.csv', 'rU') as csv_file:
	whitelabelds_reader = csv.DictReader(csv_file)

	for line in whitelabelds_reader:
		whitelabeldssegments.append(line.get('Segments'))


#end Whitelabel DS section-------------------------------------------------------------------------------------

#SFDC section------------------------------------------------------------------------------------
SFDC_IDs = []
SFDC_Owner = []
SFDC_Agency = []
SFDC_Account = []
SFDC_Opportunity = []

#SFDC = {'IDs': {'Opportunity Owner': 'Opportunity Owner', 'Agency Holding Company':'Agency Holding Company', 'Account Name':'Account Name','Opportunity Name': 'Opportunity Name', 'Product Date': 'Product Date', 'LineItemID': 'LineItemID', 'Segment Name': 'Segment Name', 'Endpoint': 'Endpoint'}}

with open('SFDC.csv', 'rU') as csv_file:
	SFDC_reader = csv.DictReader(csv_file)

	for line in SFDC_reader:
		SFDC_IDs.append(line.get('IDs'))
		SFDC_Owner.append(line.get('Opportunity Owner'))
		SFDC_Agency.append(line.get('Agency Holding Company'))
		SFDC_Account.append(line.get('Account Name'))
		SFDC_Opportunity.append(line.get('Opportunity Name'))
		#SFDC.update({line.get('IDs'): {'Opportunity Owner': line.get('Opportunity Owner'), 'Agency Holding Company':line.get('Agency Holding Company'), 'Account Name':line.get('Account Name'),'Opportunity Name': line.get('Opportunity Name'), 'Product Date': line.get('Product Date'), 'LineItemID': line.get('LineItemID'), 'Segment Name': line.get('Segment Name'), 'Endpoint': line.get('Endpoint')}})

	if len(SFDC_IDs) != len(SFDC_Owner) != len(SFDC_Agency) != len(SFDC_Account) != len(SFDC_Opportunity):
		print 'SFDC array lengths do not match'

#end SFDC section-------------------------------------------------------------------------------------

with open('hello.csv', 'rU') as csv_file:
	csv_reader = csv.DictReader(csv_file)
	if UsageReportInput == 'TTD':
		fieldnames = ['Month, Year of Month','PartnerName',	'AdvertiserName',	'CampaignName',	'TargetingDataId',	'ThirdPartyDataProviderName',	'BrandName',	'FullPath',	'ThirdPartyDataBrandId',	'SegmentId',	'ImpressionCount',	'DataCostInUSD',	'ShareThis Rev']
	elif UsageReportInput == 'Nielsen':
		fieldnames = ['Billing Month', 'Publisher', 'Segment','Publisher Revshare']
	elif UsageReportInput == 'Lotame':
		fieldnames = ['Provider Name', 'Seller Name','Buyer Name','Behavior Id','Behavior Name','Behavior Path','Revenue','Payout','Impressions','CPM','Type']
	elif UsageReportInput == 'Eyeota Branded':
		fieldnames = ['Platform', 'Buyer', 'Segment','Gross Revenue', 'rev share']
	elif UsageReportInput == 'Eyeota Whitelabel':
		fieldnames = ['Segment Supplier Category', 'Target Country Raw', 'Segment Name','Sum of Supplier Gross Earnings Final (USD)', 'Sum of Supplier Net Earnings Final (USD)']
	elif UsageReportInput == 'LiveRamp':
		fieldnames = ['REPORT_DATE', 'PLATFORM_ID', 'PLATFORM','PARTNER_NAME', 'BUYER_NAME','SOURCE','ADVERTISER_NAME','PUBLISHER','AD_ACCOUNT_ID', 'CAMPAIGN_ID', 'CAMPAIGN_NAME','CAMPAIGN_START_DATE','CAMPAIGN_END_DATE','DEVICE','AD_FORMAT','COUNTRY_DATA', 'COUNTRY_USE', 'DATA_PROVIDER_ID','LIVERAMP_SEGMENT_ID','SEGMENT_NAME', 'GROSS_DATA_CPM', 'NET_CPM', 'IMPRESSIONS', 'CLICKS','GROSS_MEDIA_SPEND','TOTAL_DATA_REVENUE_EARNED', 'DATA_PROVIDER_REVENUE','LIVERAMP_REVENUE','DATA_USE','DATA_TYPE','DATA_PROVIDER','REV_SHARE_PREMIUM_BASIC','CONVERSIONS','ATTRIBUTABLE_REVENUE','AOFT','SOURCE_ID']
	elif UsageReportInput == 'Appnexus':
		fieldnames = ['advertiser_name','buyer_member_id','buyer_member_name','campaign_id','campaign_name','data_costs','data_clearing_fee_usd','data_provider_payout_usd','data_provider_id','data_provider_name','day','geo_country','imps','month','targeted_segment_ids']
	else:
		print 'error reading headers of report'
		quit()

	if MonthInput == 'January' or MonthInput == 'February' or  MonthInput =='March':
		QuarterInput = "Q1"
	elif  MonthInput == 'April' or MonthInput =='May' or MonthInput =='June':
		QuarterInput = "Q2"
	elif  MonthInput == 'July' or MonthInput =='August' or MonthInput =='September':
		QuarterInput = "Q3"
	elif  MonthInput == 'October' or MonthInput =='November' or MonthInput =='December':
		QuarterInput = "Q4"
	
	newInputdict = {'Year' : YearInput, 'Quarter' : QuarterInput, 'Month' : MonthInput, 'Endpoint': 'need value', 'Country': 'need value', 'Region': 'needvalue', 'Integration Partner':'needvalue','Sale Type':'needvalue','Branding': 'needvalue','Segment Type': 'needvalue', 'Partner Name':'needvalue','Advertiser Name': 'needvalue','Buyer Name':'needvalue','Segment Name': 'needvalue','Revenue': 'needvalue','Segment ID': 'needvalue','Vertical Segment Name':'needvalue','Opportunity Owner':'needvalue','Agency Holding Company':'needvalue','Account Name':'needvalue','Opportunity Name':'needvalue','L1':'','L2':'','L3':'','L4':'','L5':'','L6':''} 
	with open('new_hello.csv', 'w') as csv_file:
		newheader = ['Year', 'Quarter', 'Month', 'Endpoint', 'Country', 'Region', 'Integration Partner','Sale Type','Branding','Segment Type', 'Partner Name','Advertiser Name','Buyer Name','Segment Name','Revenue','Segment ID','Vertical Segment Name','Opportunity Owner','Agency Holding Company','Account Name','Opportunity Name','L1','L2','L3','L4','L5','L6']
		csv_writer = csv.DictWriter(csv_file, fieldnames=newheader, delimiter=',')
		csv_writer.writeheader()

		for line in csv_reader:
#--------------------------------------TTD Report---------------------------------------
			if UsageReportInput == 'TTD':
				newInputdict['Endpoint']='TTD'
				#slice string to get country
				firstarrow = line['FullPath'].find(" > ")
				if line['FullPath'][:firstarrow] == 'Custom Segment' or line['FullPath'][:firstarrow] == 'Interest from Social Activity' or line['FullPath'][:firstarrow] == 'Political' or line['FullPath'][:firstarrow] == 'Winter Holiday':
					newInputdict['Region'] = 'Global'
				else:
					newInputdict['Region'] = line['FullPath'][:firstarrow]
				#print line['FullPath'][:firstarrow]
				#end country section
				newInputdict['Partner Name']= line['PartnerName']
				newInputdict['Advertiser Name']= line['AdvertiserName']
				newInputdict['Buyer Name']= 'N/A'
				newInputdict['Country']='N/A'
				#get Integration Partner
				testvalue = line['ThirdPartyDataBrandId'].find("lr")
				if testvalue > -1:
					newInputdict['Integration Partner']='Liveramp'
				else:
					newInputdict['Integration Partner']='TTD'
				#End get integration partner section

				#TTD Branding
				if line['BrandName'] == 'Data Alliance':
					newInputdict['Branding']='Unbranded'
				else:
					newInputdict['Branding']='Branded'
				#End TTD Branding

				#if SFDC_IDs.index(line['SegmentId']) > -1 or line['FullPath'].find('ShareThis > Interest from Social Activity') > -1 or line['FullPath'].find('Custom Segment >') > -1 or line['FullPath'].find('Custom >') > -1:
				if line['SegmentId'] in SFDC_IDs or line['FullPath'].find('ShareThis > Interest from Social Activity') > -1 or line['FullPath'].find('Custom Segment >') > -1 or line['FullPath'].find('Custom >') > -1:
					newInputdict['Sale Type'] = 'Direct Sales'
				else:
					newInputdict['Sale Type'] = 'BD'

				newInputdict['Segment Name']= line['FullPath']
				newInputdict['Revenue']= line['ShareThis Rev']
				newInputdict['Segment ID']= line['SegmentId']


#--------------------------------------Appnexus Report---------------------------------------
			elif UsageReportInput == 'Appnexus':

				newInputdict['Month'] = line['month']
				newInputdict['Region'] = 'N/A'
				newInputdict['Integration Partner'] = 'Appnexus'
				if line['targeted_segment_ids'] in SFDC_IDs:
					newInputdict['Sale Type'] = 'Direct Sales'
				else:
					newInputdict['Sale Type'] = 'BD'
				newInputdict['Partner Name']= 'N/A'
				newInputdict['Advertiser Name']= line['advertiser_name']
				newInputdict['Buyer Name']= line['buyer_member_name']
				newInputdict['Endpoint']='Appnexus'
				newInputdict['Country']= line['geo_country']

				if line['targeted_segment_names'].find('ShareThis') > -1:
					newInputdict['Branding']='Branded'
				else:
					newInputdict['Branding']='Unbranded'


				newInputdict['Segment Name']= line['targeted_segment_names']
				newInputdict['Revenue']= line['data_provider_payout_usd']
				newInputdict['Segment ID']= line['targeted_segment_ids']

#--------------------------------------Nielsen Report---------------------------------------
			elif UsageReportInput == 'Nielsen':

				newInputdict['Integration Partner'] = 'Nielsen'
				newInputdict['Sale Type'] = 'BD'
				newInputdict['Partner Name']= 'N/A'
				newInputdict['Advertiser Name']= 'N/A'
				newInputdict['Buyer Name']= 'N/A'

				if line['Publisher'].find('UK') > -1:
					newInputdict['Endpoint']='Nielsen EU'
					newInputdict['Region']='UK'
					newInputdict['Country'] = 'UK'
				else:
					newInputdict['Endpoint']='Nielsen US'
					newInputdict['Region']='US'
					newInputdict['Country'] = 'US'

				if line['Segment'].find('ShareThis') > -1:
					newInputdict['Branding']='Branded'
				else:
					newInputdict['Branding']='Unbranded'


				newInputdict['Segment Name']= line['Segment']
				newInputdict['Revenue']= line['Publisher Revshare']
				newInputdict['Segment ID']= 'N/A'

#--------------------------------------Lotame Report---------------------------------------
			elif UsageReportInput == 'Lotame':

				newInputdict['Region'] = 'Global'
				newInputdict['Integration Partner'] = 'Lotame'
				newInputdict['Sale Type'] = 'BD'
				newInputdict['Country']='N/A'
				newInputdict['Endpoint']='Lotame'
	
				if line['Type'].find('LDX') > -1:
					newInputdict['Branding']='Unbranded'
				elif line['Type'].find('Branded') > -1:
					newInputdict['Branding']='Branded'
				elif line['Behavior Path'].find('ShareThis') > -1:
					newInputdict['Branding']='Branded'
				else:
					newInputdict['Branding']='Unbranded'
				
				newInputdict['Partner Name']= 'N/A'
				if line['Buyer Name'] != '':
					newInputdict['Advertiser Name']= line['Buyer Name']
				else:
					newInputdict['Advertiser Name']= 'N/A'
				newInputdict['Buyer Name']= 'N/A'

				newInputdict['Segment Name']= line['Behavior Path']
				newInputdict['Revenue']= line['Payout']
				newInputdict['Segment ID']= line['Behavior Id']

#--------------------------------------Eyeota Branded Report---------------------------------------
			elif UsageReportInput == 'Eyeota Branded':
				#print line
				if line['Platform'] == 'DBM':
					newInputdict['Endpoint']= 'Doubleclick'
				else:
					newInputdict['Endpoint'] = line['Platform']
				
				newInputdict['Country']='N/A'
				
				firstarrow = line['Segment'].find(" - ")
				teststring = line['Segment'][:firstarrow]
				if teststring.find(' ShareThis') > -1:
					teststring2 = teststring.replace(' ShareThis', '')
					newInputdict['Region'] = teststring2
				else:
					newInputdict['Region'] = teststring

				newInputdict['Integration Partner'] = 'Eyeota'
				newInputdict['Sale Type'] = 'BD'
				newInputdict['Branding']='Branded'
	
				
				newInputdict['Partner Name']= 'N/A'
				newInputdict['Advertiser Name']= 'N/A'
				newInputdict['Buyer Name']= line['Buyer']

				newInputdict['Segment Name']= line['Segment']
				newInputdict['Revenue']= line['rev share']
				newInputdict['Segment ID']= 'N/A'

#--------------------------------------Eyeota Whitelabel Report---------------------------------------
			elif UsageReportInput == 'Eyeota Whitelabel':
				newInputdict['Endpoint'] = 'N/A'
				newInputdict['Country']= line['Target Country Raw']
				newInputdict['Region']= 'Global'
				newInputdict['Integration Partner'] = 'Eyeota'
				newInputdict['Sale Type'] = 'BD'
				if line['Segment Name'].find('ShareThis') > -1:
					newInputdict['Branding']='Branded'
				else:
					newInputdict['Branding']='Unbranded'
					
					
				newInputdict['Partner Name']= 'N/A'
				newInputdict['Advertiser Name']= 'N/A'
				newInputdict['Buyer Name']= 'N/A'

				newInputdict['Segment Name']= line['Segment Name']
				newInputdict['Revenue']= line['Sum of Supplier Net Earnings Final (USD)']
				newInputdict['Segment ID']= 'N/A'

#--------------------------------------LiveRamp Report---------------------------------------
			elif UsageReportInput == 'LiveRamp':
				carrot = line['SEGMENT_NAME'].find(" > ")
				arrow = line['SEGMENT_NAME'].find("-->")
				newInputdict['Endpoint'] = line['PLATFORM']
				#slice string to get country
				if arrow > -1:
					newInputdict['Country'] = 'US'
				elif line['SEGMENT_NAME'][:carrot] == 'ShareThis_US' or line['SEGMENT_NAME'][:carrot] == 'Interest from Social Activity' or line['SEGMENT_NAME'][:carrot]== 'ShareThis':
					newInputdict['Country'] = 'US'
				elif carrot == -1:
					newInputdict['Country'] = 'Check Here. No Carrot'
				elif len(line['SEGMENT_NAME'][:carrot]) > 2:
					newInputdict['Country'] = 'US'
				else:
					newInputdict['Country'] = line['SEGMENT_NAME'][:carrot]
				#end country section
				newInputdict['Region']= 'N/A'
				newInputdict['Integration Partner'] = 'Liveramp'
				
				if line['LIVERAMP_SEGMENT_ID'] in SFDC_IDs or line['SEGMENT_NAME'].find('ShareThis > Interest from Social Activity') > -1 or line['SEGMENT_NAME'].find('Custom >') > -1:
					newInputdict['Sale Type'] = 'Direct Sales'
				else:
					newInputdict['Sale Type'] = 'BD'

				newInputdict['Branding']='Branded'
				newInputdict['Partner Name']= line['SOURCE']
				
				if line['PLATFORM'] == 'Doubleclick':
					newInputdict['Advertiser Name']= line['BUYER_NAME']
				else:
					newInputdict['Advertiser Name']= line['ADVERTISER_NAME']

				newInputdict['Buyer Name']= 'N/A'
				newInputdict['Segment Name']= line['SEGMENT_NAME']
				newInputdict['Revenue']= line['DATA_PROVIDER_REVENUE']
				newInputdict['Segment ID']= line['LIVERAMP_SEGMENT_ID']

#----------------------------Start Segment Type Categorization-------------------------------


			WhitelabelDScheck = whitelabeldssegments.index(newInputdict['Segment Name']) if newInputdict['Segment Name'] in whitelabeldssegments else -1
			interestcheck = newInputdict['Segment Name'].find('Interest -')
			democheck = newInputdict['Segment Name'].find('Demographic')
			intentcheck = newInputdict['Segment Name'].find('Intent')
			B2Bcheck = newInputdict['Segment Name'].find('B2B')
			seasonalcheck1 = newInputdict['Segment Name'].find('- Seasonal -')
			seasonalcheck2 = newInputdict['Segment Name'].find('> Seasonal >')
			seasonalcheck3 = newInputdict['Segment Name'].find('Seasonal -')
			seasonalcheck4 = newInputdict['Segment Name'].find('Seasonal >')
			lifecheck = newInputdict['Segment Name'].find('Life Event')
			customcheck1 = newInputdict['Segment Name'].find('Custom >')
			customcheck3 = newInputdict['Segment Name'].find('> Custom ')
			customcheck2 = newInputdict['Segment Name'].find('> Custom >')
			customcheck4 = newInputdict['Segment Name'].find('ShareThis Custom Segment - ')
			customcheck5 = newInputdict['Segment Name'].find('Global ShareThis - Custom - ')
			customcheck6 = newInputdict['Segment Name'].find('Yahoo-->Custom ')
			customKWcheck = newInputdict['Segment Name'].find('CustomKW')
			categorycheck = newInputdict['Segment Name'].find('Category')
			verticalcheck = newInputdict['Segment Name'].find('Vertical')
			sharethischeck = newInputdict['Segment Name'].find('ShareThis')
			holidaycheck = newInputdict['Segment Name'].find('Winter Holiday >')
			#smartcheck = newInputdict['Segment Name'].find('Smart Segments')

			#if interestcheck > -1:
				#newInputdict['Segment Type'] = 'Interest'
			if newInputdict['Branding'] == 'Unbranded':

				if democheck > -1:
					if WhitelabelDScheck != -1:
						newInputdict['Segment Type'] = 'Demographic DS'
					else:
						newInputdict['Segment Type'] = 'Demographic'
				elif intentcheck > -1:
					if WhitelabelDScheck != -1:
						newInputdict['Segment Type'] = 'Intent DS'
					else:
						newInputdict['Segment Type'] = 'Intent'
				elif B2Bcheck > -1: 
					if WhitelabelDScheck != -1:
						newInputdict['Segment Type'] = 'B2B DS'
					else:
						newInputdict['Segment Type'] = 'B2B'
				elif seasonalcheck1 > -1 or seasonalcheck2 > -1 or seasonalcheck3 > -1 or seasonalcheck4 > -1 or holidaycheck > -1:
					#if newInputdict['Segment Name'].find('Holidays & Seasonal Events') > -1 or newInputdict['Segment Name'].find('Holidays and Seasonal Events') > -1:
					#	newInputdict['Segment Type'] = 'Interest'
					#else:
					newInputdict['Segment Type'] = 'Seasonal'
				elif lifecheck > -1:
					newInputdict['Segment Type'] = 'Life Event'
				# elif smartcheck > -1: 
				# 	if WhitelabelDScheck != -1:
				# 		newInputdict['Segment Type'] = 'Smart DS'
				# 	else:
				# 		newInputdict['Segment Type'] = 'Smart'
				elif customcheck1 > -1 or customcheck2 > -1 or customcheck3 > -1 or customKWcheck > -1 or customcheck4 > -1 or customcheck5 > -1 or customcheck6 > -1:
					newInputdict['Segment Type'] = 'Custom'
				elif categorycheck >-1  or verticalcheck > -1 or sharethischeck > -1:
					newInputdict['Segment Type'] = 'Interest'
				else:
					newInputdict['Segment Type'] = 'Interest'
				if UsageReportInput == 'Eyeota Whitelabel':
					if line['Segment Supplier Category'] == 'Custom':
						newInputdict['Segment Type']= 'Custom'
					else:
						pass
#----------------------------branded Categorization---------------------------------------------------
			else:
				if seasonalcheck1 > -1 or seasonalcheck2 > -1 or seasonalcheck3 > -1 or seasonalcheck4 > -1 or holidaycheck > -1:
					#if newInputdict['Segment Name'].find('Holidays & Seasonal Events') > -1 or newInputdict['Segment Name'].find('Holidays and Seasonal Events') > -1:
					#	newInputdict['Segment Type'] = 'Vertical'
					#else:
					newInputdict['Segment Type'] = 'Seasonal'
				elif lifecheck > -1:
					newInputdict['Segment Type'] = 'Life Event'
				elif customcheck1 > -1 or customcheck2 > -1 or customcheck3 > -1 or customKWcheck > -1 or customcheck4 > -1 or customcheck5 > -1 or customcheck6 > -1:
					newInputdict['Segment Type'] = 'Custom'
				elif categorycheck >-1  or verticalcheck > -1 or sharethischeck > -1:
					newInputdict['Segment Type'] = 'Vertical'
				else:
					newInputdict['Segment Type'] = 'Vertical'

				if UsageReportInput == 'Eyeota Whitelabel':
					if line['Segment Supplier Category'] == 'Custom':
						newInputdict['Segment Type']= 'Custom'
				else:
					pass
				
					
			#End Segment Type Categorization
#----------------------------Start SFDC data input-------------------------------
			if newInputdict['Segment ID'] in SFDC_IDs:
				check = newInputdict['Segment ID']
				findspot = SFDC_IDs.index(check)
				newInputdict['Opportunity Owner'] = SFDC_Owner[findspot]
				newInputdict['Agency Holding Company'] = SFDC_Agency[findspot]
				newInputdict['Account Name'] = SFDC_Account[findspot]
				newInputdict['Opportunity Name'] = SFDC_Opportunity[findspot]
			else:
				newInputdict['Opportunity Owner'] = '-'
				newInputdict['Agency Holding Company'] = '-'
				newInputdict['Account Name'] = '-'
				newInputdict['Opportunity Name'] = '-'
#----------------------------End SFDC data input-------------------------------

#----------------------------Start L1 Category splits-------------------------------
			arrow = newInputdict['Segment Name'].find("-->")
			longarrow = newInputdict['Segment Name'].find(" ---> ")
			string = newInputdict['Segment Name']

			if longarrow > -1:
				string = string.replace(' ---> ', ' > ')
				split1 = string.find('Activity >')
				split2 = string.find('ShareThis_US')
				split3 = string.find('ShareThis')
				if  split1 > -1:
					string = string[split1:]
				elif split2 > -1:
					newnum = split2 + 15
					string = string[newnum:]
				elif split3 > -1:
					newnum = split3 + 12
					string = string[newnum:]
			elif arrow > -1:
				string = string.replace('-->', ' > ')
				split1 = string.find('Activity >')
				split2 = string.find('ShareThis_US')
				split3 = string.find('ShareThis')
				if  split1 > -1:
					string = string[split1:]
				elif split2 > -1:
					newnum = split2 + 15
					string = string[newnum:]
				elif split3 > -1:
					newnum = split3 + 12
					string = string[newnum:]



			carrotcheck = string.find(' > ')
			dashcheck = string.find(' - ')
			hatcheck = string.find('^')
			sharecheck = string.find('Interest from Social Activity - ')
			activitycheck = string.find('Activity >')
			eyeotacheck = string.find('Eyeota Reach')

			if hatcheck > -1:
				symboltosplit = '^'
				numsplit = 1
			elif dashcheck > -1:
				symboltosplit = ' - '
				numsplit = 3
			elif carrotcheck > -1:
				symboltosplit = ' > '
				numsplit = 3
			else:
				print 'No symbol to split'
				symboltosplit = 'no symbol'
				numsplit = 0
			#print string
			if symboltosplit == 'no symbol':
				newInputdict['Vertical Segment Name'] = string
			elif activitycheck > -1:
				newnum = activitycheck + 11
				newInputdict['Vertical Segment Name'] = string[newnum:]
			elif sharecheck > -1:
				newnum = sharecheck + 32
				newInputdict['Vertical Segment Name'] = string[newnum:]
			elif eyeotacheck > -1:
				newnum = eyeotacheck + 15
				newInputdict['Vertical Segment Name'] = string[newnum:]
			else:
				split0 = string.find(symboltosplit)
				newnum = split0 + numsplit
				newInputdict['Vertical Segment Name'] = string[newnum:]

			string = newInputdict['Vertical Segment Name']

			#clean up Vertical name section for Custom segments in Liveramp and TTD Reports
			activitycheck = string.find('Activity > ')
			onecheck = string.find('> 1')

			if activitycheck > -1 and onecheck > -1:
				newnum = activitycheck + 11
				newstring = string[newnum:]
				#newnum2 = onecheck
				onecheck = newstring.find(' > 1')
				string = newstring[:onecheck]
			elif activitycheck >-1:
				newnum = activitycheck + 11
				string = string[newnum:]
			elif onecheck > -1:
				string = string[:onecheck]

			#End clean up vertical name sectionfor Custom segments in Liveramp and TTD Reports

			split1 = string.find(symboltosplit)

			if split1 > -1:
				newnum = split1 + numsplit
				newInputdict['L1'] = string[:split1]
				string = string[newnum:]
				split2 = string.find(symboltosplit)
			else:
				newInputdict['L1'] = string
				newnum = 0
				string = ''
				split2 = string.find(symboltosplit)

			if split2 > -1:
				newInputdict['L2'] = string[:split2]
				newnum = split2 + numsplit
				string = string[newnum:]
				split3 = string.find(symboltosplit)
				if split3 > -1:
					newInputdict['L3'] = string[:split3]
					newnum = split3 + numsplit
					string = string[newnum:]
					split4 = string.find(symboltosplit)
					if split4 > -1:
						newInputdict['L4'] = string[:split4]
						newnum = split4 + numsplit
						string = string[newnum:]
						split5 = string.find(symboltosplit)
						if split5 > -1:
							newInputdict['L5'] = string[:split5]
							newnum = split5 + numsplit
							string = string[newnum:]
							split6 = string.find(symboltosplit)
							if split6 > -1:
								newInputdict['L6'] = string[:split6]
							else:
								newnum = split5 + numsplit
								newInputdict['L6'] = string
						else: 
							newnum = split5 + numsplit
							newInputdict['L5'] = string
							newInputdict['L6'] = ''
					else:
						newnum = split4 + numsplit
						newInputdict['L4'] = string
						newInputdict['L5'] = ''
						newInputdict['L6'] = ''
				else:
					newnum = split3 + numsplit
					newInputdict['L3'] = string
					newInputdict['L4'] = ''
					newInputdict['L5'] = ''
					newInputdict['L6'] = ''
			else:
				newnum = split2 + numsplit
				newInputdict['L2'] = string
				newInputdict['L3'] = ''
				newInputdict['L4'] = ''
				newInputdict['L5'] = ''
				newInputdict['L6'] = ''

#--------------------------write to CSV-------------------------------------------
			csv_writer.writerow(newInputdict)
		