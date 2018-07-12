from google.cloud import bigquery
import csv

def DSsegments():
#----------------------------------------get DS segments data---------------------------------------------
	client = bigquery.Client.from_service_account_json('/Users/sheldonchang/desktop/scriptstuff/secrets.json')

	job_config = bigquery.QueryJobConfig()
	job_config.use_legacy_sql = True

	DSsegmentsarray = []

	query_job2 = client.query("""
		select row_number() over() row_number, * from (
		select name, destinations from
		(select _id, name, group_concat(destinations.name) destinations from 
		    TABLE_DATE_RANGE(dmp_meta.segments_def_v2_ ,
		    DATE_ADD(CURRENT_TIMESTAMP(), -2, 'DAY'),DATE_ADD(CURRENT_TIMESTAMP(), -2, 'DAY'))  group by _id, name
		) a join
		(select segment_id  from 
		TABLE_DATE_RANGE(dmp.model_segments_v3_processed_,DATE_ADD(CURRENT_TIMESTAMP(), -2, 'DAY'),DATE_ADD(CURRENT_TIMESTAMP(), -2, 'DAY'))
		group by segment_id )b
		on
		a._id=b.segment_id
		order by name
		)""",    location='US',
	    job_config=job_config)

	results2 = query_job2.result()



	with open('DSsegments.csv', 'w', encoding='ISO-8859-1') as DSsegments_file:
		DSsegments_writer = csv.writer(DSsegments_file, delimiter='\t')

		for row in results2:
			DSsegments_writer.writerow([row[1]])
	print('DS segments was successful')
	DSsegments_file.close()

