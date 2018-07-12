from google.cloud import bigquery

client = bigquery.Client.from_service_account_json('/Users/sheldonchang/desktop/scriptstuff/secrets.json')


#----------------------------------------get DS segments data---------------------------------------------
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
	)""")

results2 = query_job2.result()

for row in results2:
	print(row)