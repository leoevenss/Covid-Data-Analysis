import pandas as pd
import urllib, json
import csv
import datetime
import statistics 

#loading week data
fields=['districtid','weekid','cases']
weekdata=pd.read_csv('cases-week.csv',usecols=fields)


#loading month data
fields=['districtid','monthid','cases']
monthdata=pd.read_csv('cases-month.csv',usecols=fields)


#loading overall data
fields=['districtid','overallid','cases']
overalldata=pd.read_csv('cases-overall.csv',usecols=fields)


#loading edge graph data
edgelist=[]
with open('edge-graph.csv', 'r') as data: 
      
    for line in csv.reader(data): 
        edgelist.append(line)

#removing the heading
edgelist.pop(0)

#creating dictionary of neigbor district cases
neibordict=dict()
for i in range(101,729):
    for l in edgelist:
        if i==int(l[0]):
            neibordict.setdefault(i,[]).append(l[1])
        elif i==int(l[1]):
            neibordict.setdefault(i,[]).append(l[0])



#calculating week wise mean
weeklist=[]
weekmeandict={}
weekstddict={}
for weekid in range(1,26):
    for key,value in neibordict.items():
        for nei in value:
            cases=int(weekdata.loc[(weekdata['weekid']==weekid) & (weekdata['districtid']==int(nei)) ]['cases'])
            weeklist.append(cases)
            weekm=round(statistics.mean(weeklist),2)
            if(len(weeklist)>1):
                weekst=round(statistics.stdev(weeklist),2)
            else:
                weekst=0
        
        weekmeandict.setdefault(key,[]).append(weekm)
        
        weekstddict.setdefault(key,[]).append(weekst)
        weeklist=[]





#writing week wise result
with open('neighbor-week.csv', mode='w', newline='') as csv_file:
    csv_writer = csv.writer(csv_file)
    csv_writer.writerow(['districtid','weekid','neighbormean','neighborstdev'])
    
    for (k,v), (k2,v2) in zip(weekmeandict.items(), weekstddict.items()):
        for weekid in range(25):
            mean=v[weekid]
            std=v2[weekid]
            csv_writer.writerow([k,weekid+1,mean,std])

#calculating month wise result
monthlist=[]
monthmeandict={}
monthstddict={}
for monthid in range(1,8):
    for key,value in neibordict.items():
        for nei in value:
            cases=int(monthdata.loc[(monthdata['monthid']==monthid) & (monthdata['districtid']==int(nei)) ]['cases'])
            monthlist.append(cases)
            monthm=round(statistics.mean(monthlist),2)
            if(len(monthlist)>1):
                monthst=round(statistics.stdev(monthlist),2)
            else:
                monthst=0
        
        monthmeandict.setdefault(key,[]).append(monthm)
        
        monthstddict.setdefault(key,[]).append(monthst)
        monthlist=[]





#writing monthwise result
with open('neighbor-month.csv', mode='w', newline='') as csv_file:
    csv_writer = csv.writer(csv_file)
    csv_writer.writerow(['districtid','monthid','neighbormean','neighborstdev'])
    
    for (k,v), (k2,v2) in zip(monthmeandict.items(), monthstddict.items()):
        for monthid in range(7):
            mean=v[monthid]
            std=v2[monthid]
            csv_writer.writerow([k,monthid+1,mean,std])

#calculating overall results
overalllist=[]
overallmeandict={}
overallstddict={}

for key,value in neibordict.items():
    for nei in value:
        cases=int(overalldata.loc[(overalldata['overallid']==1) & (overalldata['districtid']==int(nei)) ]['cases'])
        overalllist.append(cases)
        overallm=round(statistics.mean(overalllist),2)
        if(len(overalllist)>1):
            overallst=round(statistics.stdev(overalllist),2)
        else:
            overallst=0
        
    overallmeandict.setdefault(key,[]).append(overallm)
        
    overallstddict.setdefault(key,[]).append(overallst)
    overalllist=[]





#writing overall results
with open('neighbor-overall.csv', mode='w', newline='') as csv_file:
    csv_writer = csv.writer(csv_file)
    csv_writer.writerow(['districtid','overallid','neighbormean','neighborstdev'])
    
    for (k,v), (k2,v2) in zip(overallmeandict.items(), overallstddict.items()):
        mean=v[0]
        std=v2[0]
        csv_writer.writerow([k,1,mean,std])








