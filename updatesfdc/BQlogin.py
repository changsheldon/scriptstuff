from google.cloud import bigquery

def BQdata():
	client = bigquery.Client.from_service_account_json('/Users/sheldonchang/desktop/scriptstuff/secrets.json')


	query_job = client.query("""
	#standardsql
	select destination_seg_id, name, destination_name   from delivery.segments_count_with_name
	where 
	kind ="custom"
	group by destination_seg_id, name, destination_name
	order by name""")

	results = query_job.result()

	TTDData = {}
	AppnexusData = {}
	EyeotaData = {}
	#Data2 = []
	for row in results:
		if row[2] == 'ttd':
			TTDData[row[1]] = {'ID' : row[0], 'Endpoint': row[2]}
		elif row[2] == 'eyeota':
			EyeotaData[row[1]] = {'ID' : row[0], 'Endpoint': row[2]}
		#elif row[2] == 'appnexus':
		#	AppnexusData[row[1]] = {'ID' : row[0], 'Endpoint': row[2]}
		else:
			pass
		#print(results['destination_name'])
	#print(Data)

	# for entries in Data:
	# 	print(Data[entries])
	#print(Data)
	#return TTDData,EyeotaData,AppnexusData
	print('BQ login successful')
	return TTDData,EyeotaData