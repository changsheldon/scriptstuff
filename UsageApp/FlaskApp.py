from flask import Flask, render_template, request, flash, g, redirect,url_for, send_from_directory
from flask_login import LoginManager
from flask_uploads import UploadSet, configure_uploads, DATA
import os
import csv
import time
from formatscripts import *

app = Flask(__name__)

app.config['UPLOADED_CSVFILES_DEST'] = 'app/uploadfile'
csvfiles = UploadSet('csvfiles', ('csv'))
configure_uploads(app, (csvfiles))



@app.route("/")
# @app.route("/home")
# def home():
# 	return render_template('home.html', posts=posts)

# @app.route("/about")
# def about():
# 	return render_template('about.html', title='About')


@app.route("/index")
def index():
	return render_template('upload.html', title='Upload Usage')

# @app.route("/show")
# def show():
# 	return render_template('show.html', title='File Uploaded')

@app.route('/upload', methods=['GET', 'POST'])
def upload():
	if request.method == 'POST':
		ReportDict = ["Nielsen", "Eyeota Branded", "Eyeota Whitelabel", "LiveRamp", "TTD", "Lotame", "Appnexus"]
		try:
			reportinginput = request.form['reportinginput']
			MonthInput = request.form['MonthInput']
			YearInput = request.form['YearInput']
			thefile = request.files['csvfile']
			thepath = os.path.join(app.config['UPLOADED_CSVFILES_DEST'],thefile.filename)
			thefile.save(thepath)
			thefilename = thefile.filename
			hardcodeUpdateInput = 'y'

		except KeyError as e:
			message = "An input was blank"
			return render_template('upload.html', title='Upload Usage', message=message)
			
		else:
			if reportinginput not in ReportDict:
				
				message = "Please input a valid Usage Report"
				return render_template('upload.html', title='Upload Usage', message=message)
			else:
				check = testfunction(thepath,reportinginput)
				if check[0] == 'not valid':
					print(check[1])
					message = 'These headers are not in the report ---> '
					string2 = ''
					for thing in check[1]:
						message = message + thing + ', '
					return render_template('upload.html', title='Upload Usage', message=message)
				else:

					return redirect(url_for('process',hardcodeUpdateInput=hardcodeUpdateInput , thepath = thepath,reportinginput=reportinginput ,MonthInput=MonthInput,YearInput=YearInput))
					
# @app.route('/processing', methods=['GET', 'POST'])
# def processing(hardcodeUpdateInput, thepath,reportinginput,MonthInput,YearInput):
# 	reportinginput = request.args.get('reportinginput')
# 	MonthInput = request.args.get('MonthInput')
# 	YearInput = request.args.get('YearInput')
# 	#thefile = request.files['csvfile']
# 	thepath = request.args.get('thepath')
# 	#thefilename = thefile.filename
# 	hardcodeUpdateInput = request.args.get('hardcodeUpdateInput')
	
# 	formatusage.formatusage(hardcodeUpdateInput, thepath,reportinginput ,MonthInput,YearInput)
# 	return render_template('complete.html', title='Upload Usage', message=message)
				
@app.route('/process', methods=['GET', 'POST'])
def process():
	if request.method == 'POST':
	#processing(hardcodeUpdateInput, thepath,reportinginput,MonthInput,YearInput)
		render_template('process.html', title='Processing Report')
	else:
	
		reportinginput = request.args.get('reportinginput')
		MonthInput = request.args.get('MonthInput')
		YearInput = request.args.get('YearInput')
		thepath = request.args.get('thepath')
		hardcodeUpdateInput = request.args.get('hardcodeUpdateInput')
		#return redirect(url_for('processing',hardcodeUpdateInput=hardcodeUpdateInput , thepath = thepath,reportinginput=reportinginput ,MonthInput=MonthInput,YearInput=YearInput))
		message = formatusage.formatusage(hardcodeUpdateInput, thepath,reportinginput ,MonthInput,YearInput)
		return render_template('complete.html', title='Upload Usage', message=message)

def testfunction(thepath,reportinginput):
	# had to escape quotes and do extra formatting to incorporate "Month, Year of Month" because of comma split
	headers = {
		'TTD':['\"Month', ' Year of Month\"','Partner',	'Advertiser',	'Campaign',	'TargetingDataId',	'BrandName',	'FullPath',	'ThirdPartyDataBrandId',	'SegmentId',	'ShareThis Rev'],
		'Nielsen':['Month', 'Publisher', 'Segment','Revenue', 'Network', 'Platform'],
		'Lotame':['Provider Name', 'Seller Name','Buyer Name','Behavior Id','Behavior Name','Behavior Path','Revenue','Payout','Impressions','CPM','Type'],
		'Eyeota Branded':['Platform', 'Buyer', 'Segment','Gross Revenue', 'rev share'],
		'Eyeota Whitelabel':['Segment Supplier Category', 'Target Country Raw', 'Segment Name','Sum of Supplier Gross Earnings Final (USD)', 'Sum of Supplier Net Earnings Final (USD)'],
		'LiveRamp':['REPORT_DATE', 'PLATFORM_ID', 'PLATFORM','PARTNER_NAME', 'BUYER_NAME','SOURCE','ADVERTISER_NAME','PUBLISHER','AD_ACCOUNT_ID', 'CAMPAIGN_ID', 'CAMPAIGN_NAME','CAMPAIGN_START_DATE','CAMPAIGN_END_DATE','DEVICE','AD_FORMAT','COUNTRY_DATA', 'COUNTRY_USE', 'DATA_PROVIDER_ID','LIVERAMP_SEGMENT_ID','SEGMENT_NAME', 'GROSS_DATA_CPM', 'NET_CPM', 'IMPRESSIONS', 'CLICKS','GROSS_MEDIA_SPEND','TOTAL_DATA_REVENUE_EARNED', 'DATA_PROVIDER_REVENUE','LIVERAMP_REVENUE','DATA_USE','DATA_TYPE','DATA_PROVIDER','REV_SHARE_PREMIUM_BASIC','CONVERSIONS','ATTRIBUTABLE_REVENUE','AOFT','SOURCE_ID'],
		'Appnexus':['advertiser_name','buyer_member_id','buyer_member_name','campaign_id','campaign_name','data_costs','data_clearing_fee_usd','data_provider_payout_usd','data_provider_id','data_provider_name','day','geo_country','imps','month','targeted_segment_ids'],
	}
	fixheader = []
	headercheck = 'valid'
	with open(thepath, 'r', encoding='ISO-8859-1') as f:
		#reader = csv.DictReader(f)
		hello = []
		f_header = f.readline()
		preheader = f_header.split(',')
		for stuff in preheader:
			hello.append(stuff.strip())
		#newheader = preheader.strip()
		#print(newheader)
		for thing in headers[reportinginput]:
			if thing not in hello:
				print(thing)
				fixheader.append(thing)
				headercheck = 'not valid'
			else:
				#print('header found')
				pass
		if headercheck == 'not valid':
		# 	print('These headers are not in the report ---> ', fixheader)
			message = 'These headers are not in the report ---> ', fixheader
		# 	return headercheck,
		else:
			message = 'Headers look good!'
		# 	return render_template('upload.html', title='Upload Usage', message=message)
		
		return headercheck, fixheader


@app.route('/downloadFormatted', methods=['GET', 'POST'])
def downloadformatted():
	path2 = '/Users/sheldonchang/Desktop/scriptstuff/UsageApp/app/uploadfile/'
	return send_from_directory(path2,'FormattedReport.csv', as_attachment=True)

@app.route('/downloadchanged', methods=['GET', 'POST'])
def downloadchanged():
	path2 = '/Users/sheldonchang/Desktop/scriptstuff/UsageApp/app/uploadfile/'
	return send_from_directory(path2,'changed_SFDC.csv', as_attachment=True)

@app.route('/complete', methods=['GET', 'POST'])
def complete():
	
	return render_template('complete.html', title='Upload Usage')


# @app.route('/upload/<id>')
# def show(id):
#     csvfiles = csvfile.load(id)
#     if csvfiles is None:
#         abort(404)
#     url = photos.url(csvfiles.filename)
#     return render_template('show.html', url=url, photo=csvfiles)


if __name__ == '__main__':
	app.run(debug=True)

	#app.config['SECRET_KEY'] = random()
	#app.secret_key = random()