import requests

AppData = {}

url = 'https://data-api.sharethis.com/v1.0/audiences/appnexus-ids.csv?token=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJfaWQiOiI1OTQxYjNiNTQ2NzZiMDAwMTI4ZGY1NDIiLCJlbWFpbCI6InNoZWxkb25Ac2hhcmV0aGlzLmNvbSJ9.IW0niZM_xXZJZmWzwDegqIC6U2bUu0IUzENufXEcCA4'
req = requests.get(url)

row = req.text.split('\n')


for line in row:
	oh = line.split(',')
	try:
		if oh[1].find('ShareThis') > -1:
			AppData[oh[1]] = oh[2]
	except IndexError as e:
		print(oh)
		print(e)
	else:
		pass