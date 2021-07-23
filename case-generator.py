import pandas as pd
import urllib, json
import csv
import datetime


#loading the data
fields=['Date','District','Cases']
data=pd.read_csv('alldata_base.csv',usecols=fields)
data['Date']=pd.to_datetime(data['Date'])

data['overallid']=0


data.reset_index(inplace=True)



#writing overall data

overall=data.groupby(['District']).sum()

overall.reset_index(inplace=True)

overall['overallid']=1

overall=overall.drop(['index'],axis=1)





with open('cases-overall.csv', mode='a', newline='') as csv_file:
    csv_writer = csv.writer(csv_file)
    csv_writer.writerow(['districtid','overallid','cases'])
    for i in range(len(overall)):
        csv_writer.writerow([overall.iloc[i,0],overall.iloc[i,2],overall.iloc[i,1]])

data=data.drop(['overallid'],axis=1)

#writing monthwise data

data['monthid']=0



monthdict=data.to_dict('index')





monthls=[30,31,30,31,31,5]

i=datetime.datetime(2020, 3, 15)
j=datetime.datetime(2020, 3, 31)


monid=1
i=datetime.datetime(2020, 3, 15)
j=datetime.datetime(2020, 3, 31)
for key,value in monthdict.items():
        if value['Date']>=i and value['Date']<=j:
            value['monthid']=monid

monid=2

for l in monthls:    
    i=j+datetime.timedelta(days=+1)
    j+=datetime.timedelta(days=+l)
    for key,value in monthdict.items():
        if value['Date']>=i and value['Date']<=j:
            value['monthid']=monid
    
        
    monid+=1



monthdf=pd.DataFrame.from_dict(monthdict)

monthdf=monthdf.transpose()


monthdf=monthdf.drop(['index'],axis=1)



monthdf=monthdf.groupby(['District','monthid']).sum()



monthdf.reset_index(inplace=True)



with open('cases-month.csv', mode='a', newline='') as csv_file:
    csv_writer = csv.writer(csv_file)
    csv_writer.writerow(['districtid','monthid','cases'])
    for i in range(len(monthdf)):
        csv_writer.writerow([monthdf.iloc[i,0],monthdf.iloc[i,1],monthdf.iloc[i,2]])


data=data.drop(['monthid'],axis=1)

#writing weekwise

data['weekid']=0

weekid=data.to_dict('index')



wkid=1
i=datetime.datetime(2020, 3, 15)
j=datetime.datetime(2020, 3, 21)

for b in range(25):    
    for key,value in weekid.items():
        if value['Date']>=i and value['Date']<=j:
            value['weekid']=wkid
    i+=datetime.timedelta(days=7)
    j+=datetime.timedelta(days=7)
    wkid+=1

weekdf=pd.DataFrame.from_dict(weekid)

weekdf=weekdf.transpose()
weekdf=weekdf.drop(['index'],axis=1)



weekdf=weekdf.groupby(['District','weekid']).sum()



weekdf.reset_index(inplace=True)



with open('cases-week.csv', mode='a', newline='') as csv_file:
    csv_writer = csv.writer(csv_file)
    csv_writer.writerow(['districtid','weekid','cases'])
    for i in range(len(weekdf)):
        csv_writer.writerow([weekdf.iloc[i,0],weekdf.iloc[i,1],weekdf.iloc[i,2]])




