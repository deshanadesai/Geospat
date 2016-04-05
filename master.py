import pandas as pd
import glob  
import csv
import os

# read data  
with open('masterfile.csv','wb') as fp:
	writer = csv.writer(fp,delimiter=',')
	writer.writerow(['index','time','lat','lon','elevation','accuracy','bearing','speed','satellites','provider','data','Hours','Day','ID'])
for datafile in glob.glob("attachments/*.csv"): 
	data = pd.read_csv(datafile)
	base=os.path.basename(datafile)
	basename = os.path.splitext(base)[0]
	basename = basename.split('@')[0]
	data['ID'] = basename
	data['date'] = data.time.map(lambda x: x.split('T')[0])
	data['time'] = pd.to_datetime(data.time)
	data['Hours'] = data.time.map(lambda x: x.hour)
	data['Day'] = data.time.map(lambda x: x.day)
	with open('masterfile.csv','ab') as fp:
		data.to_csv(fp,header = False)

