import pandas as pd
import glob  
import csv
import os

def num_holes(uid,day):
	data = pd.read_csv('masterfile.csv')
	data = data.loc[data['ID']== uid]
	data = data.loc[data['Day']== day]
	data = data.sort('time')
	print "Subject Name: ",uid
	#print data
	if data.shape[0]>1:
		print "Starting time: ",data.iat[0,1]
		start = data.iat[0,1]
		row = data.shape[0]
		row = row - 1
		print "Ending time: ",data.iat[row,1]
		end = data.iat[row,1]
		print "Number of data points: ",data.shape[0]
		numpts = data.shape[0]
		writer.writerow([uid,start,end,numpts])

import datetime
import numpy as np

'''def heatmap(uid,day):
	fields = ['time','ID','Day']
	data = pd.read_csv('masterfile.csv',usecols=fields)
	data['hole']  = 1

	df = data.loc[data['Day']== day]
	data = df.loc[df['ID']== uid]
	data['time'] = pd.to_datetime(data.time)

	for x in data['time']:
		mod_time = x.replace(second=0, microsecond=0)
		i = data.loc[data['time']==x].index
		data.set_value(i, 'time', mod_time)

	data = data.sort('time')
	start = data.iat[0,0]
	nextt = start + datetime.timedelta(minutes=1)
	print data.shape
	data.drop_duplicates(inplace=True)
	ctr = 3000
	for x in range(0,20):
		if any(data['time']!=x):
			d = {'time':nextt,'Day':day,'ID':uid,'hole':0}
			df2 = pd.DataFrame(data=d,index=[ctr])
			ctr = int(ctr)+1
			print "herer"
			data.append(df2, ignore_index = True) #hole present
		nextt = nextt + datetime.timedelta(minutes = 1)

	print data.shape
	print start
	print nextt'''

df = pd.read_csv('masterfile.csv')
#heatmap('bhardwaj.rish',4)
print "Number of subjects: ",len(df['ID'].unique())
print "Summary: \n",pd.value_counts(df['ID'].values)
for day in df['Day'].unique():
	daynum = "Day "+str(day)+".csv"
	with open(daynum,'wb') as filename:
		writer = csv.writer(filename)
		writer.writerow(['ID','Starting Time','Ending Time','Number of data points'])
		for uid in df['ID'].unique():
			num_holes(uid,day)