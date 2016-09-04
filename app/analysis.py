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
		print "Average Accuracy: ",data['accuracy'].mean()
		avg_acc = data['accuracy'].mean()
		median_acc = data['accuracy'].median()
		writer.writerow([uid,start,end,numpts,avg_acc,median_acc])

import datetime
import numpy as np

def heatmap(day):
	fields = ['time','ID','Day']
	df = pd.read_csv('masterfile.csv',usecols = fields)
	df['hole'] = 1

	datalists = []

	for uid in df['ID'].unique():
		dfsplit = df.loc[df['ID']==uid]
		dfsplit['time'] = pd.to_datetime(dfsplit.time)
		datalists.append(dfsplit)

	start = datetime.datetime(2016,4,day,0,0,0)
	stop = datetime.datetime(2016,4,day,23,59,0)

	ctr = True
	while(start!=stop):
		start = start+datetime.timedelta(minutes = 1)
		for data in datalists:
			if any(data['time']== start) or any(data['time']-start<datetime.timedelta(minutes=1)):
				continue
			else:
				uid = data['ID'].unique()
				df1 = pd.DataFrame({'time':start,'Day':day,'ID': uid[0],'hole':0},index=[0])
				if ctr:
					frames = [df1]
					ctr = False
				else:
					frames = [df1,result]
				result = pd.concat(frames)
	
	for data in datalists:
		frames = [data,result]
		result = pd.concat(frames)

	result.to_csv("holesheet.csv")

def accuracy_heatmap(day):
	result = pd.read_csv("masterfile.csv")
	result = result.loc[result['Day']==day]
	result = result.pivot("ID","time","accuracy")
	ax = sns.heatmap(result)
	sns.plt.show()

import seaborn as sns
import matplotlib as plt
'''
result = pd.read_csv("holesheet.csv")
result = result.pivot("ID","time","hole")
ax = sns.heatmap(result)
sns.plt.show()'''

accuracy_heatmap(4)


'''
df = pd.read_csv('masterfile.csv')
heatmap(4)'''
'''
print "Number of subjects: ",len(df['ID'].unique())
print "Summary: \n",pd.value_counts(df['ID'].values)
for day in df['Day'].unique():
	daynum = "Day "+str(day)+".csv"
	with open(daynum,'wb') as filename:
		writer = csv.writer(filename)
		writer.writerow(['ID','Starting Time','Ending Time','Number of data points','Mean Accuracy','Median Accuracy'])
		for uid in df['ID'].unique():
			num_holes(uid,day)'''
