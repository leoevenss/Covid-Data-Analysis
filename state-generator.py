import pandas as pd
import urllib, json
import csv
import datetime
import statistics 
import collections

#loading all case data file
fields=['State','District']
statedata=pd.read_csv('alldata_base.csv',usecols=fields)


#grouping by state and district cases
groupindata=statedata.groupby(['State','District']).sum()

groupindata.reset_index(inplace=True)

statedict={}
for i in range(len(groupindata)):
    statedict.setdefault(groupindata['State'][i],[]).append(groupindata['District'][i])

#groupindata.columns

#len(statedict)

#loading week data
fields=['districtid','weekid','cases']
weekdata=pd.read_csv('cases-week.csv',usecols=fields)


#loading month data
fields=['districtid','monthid','cases']
monthdata=pd.read_csv('cases-month.csv',usecols=fields)


#loading overall data
fields=['districtid','overallid','cases']
overalldata=pd.read_csv('cases-overall.csv',usecols=fields)


#extracting data weekwise into dictionary
weekcaselist=[]
weekdict={}
for i in range(101,728):
    for weekid in range(1,26):
        weekcases=int(weekdata.loc[(weekdata['weekid']==weekid) & (weekdata['districtid']==int(i)) ]['cases'])
        weekcaselist.append(weekcases)
    
    weekdict[i]=weekcaselist
    weekcaselist=[]

#extracting data monthwise into dictionary
monthcaselist=[]
monthdict={}
for i in range(101,728):
    for monthid in range(1,8):
        monthcases=int(monthdata.loc[(monthdata['monthid']==monthid) & (monthdata['districtid']==int(i)) ]['cases'])
        monthcaselist.append(monthcases)
    
    monthdict[i]=monthcaselist
    monthcaselist=[]

#extracting data overall into dictionary
overallcaselist=[]
overalldict={}
for i in range(101,728):
        overallcases=int(overalldata.loc[(overalldata['overallid']==1) & (overalldata['districtid']==int(i)) ]['cases'])
        overallcaselist.append(overallcases)
    
        overalldict[i]=overallcaselist
        overallcaselist=[]







#for week result
weekmeandict={}
weekstddict={}
weekneiblist=[]
for wkid in range(25):
    for key,value in statedict.items():
        for v in value:
            weekneiblist.append(weekdict[v][wkid])
        for v in value:
            weekneiblist.remove(weekdict[v][wkid])
           
            if(len(weekneiblist)>=1):
                weekmean=round(statistics.mean(weekneiblist),2)
            else:
                weekmean=0
        
            
            if(len(weekneiblist)>1):
                weekstd=round(statistics.stdev(weekneiblist),2)
            else:
                weekstd=0
            weekneiblist.append(weekdict[v][wkid])
            weekmeandict.setdefault(v,[]).append(weekmean)
            weekstddict.setdefault(v,[]).append(weekstd)
        weekneiblist=[]

weekmeandict = collections.OrderedDict(sorted(weekmeandict.items()))
weekstddict = collections.OrderedDict(sorted(weekstddict.items()))

with open('state-week.csv', mode='w', newline='') as csv_file:
    csv_writer = csv.writer(csv_file)
    csv_writer.writerow(['districtid','weekid','statemean','statestdev'])
    
    for (k,v), (k,v2) in zip(weekmeandict.items(), weekstddict.items()):
        for weekid in range(25):
            wmean=v[weekid]
            wstd=v2[weekid]
            csv_writer.writerow([k,weekid+1,wmean,wstd])

#for month results
monthmeandict={}
monthstddict={}
monthneiblist=[]
for mnid in range(7):
    for key,value in statedict.items():
        for v in value:
            monthneiblist.append(monthdict[v][mnid])
        for v in value:
            monthneiblist.remove(monthdict[v][mnid])
           
            if(len(monthneiblist)>=1):
                monthmean=round(statistics.mean(monthneiblist),2)
            else:
                monthmean=0
        
            
            if(len(monthneiblist)>1):
                monthstd=round(statistics.stdev(monthneiblist),2)
            else:
                monthstd=0
            monthneiblist.append(monthdict[v][mnid])
            monthmeandict.setdefault(v,[]).append(monthmean)
            monthstddict.setdefault(v,[]).append(monthstd)
        monthneiblist=[]

monthmeandict = collections.OrderedDict(sorted(monthmeandict.items()))
monthstddict = collections.OrderedDict(sorted(monthstddict.items()))

with open('state-month.csv', mode='w', newline='') as csv_file:
    csv_writer = csv.writer(csv_file)
    csv_writer.writerow(['districtid','monthid','statemean','statestdev'])
    
    for (k,v), (k,v2) in zip(monthmeandict.items(), monthstddict.items()):
        for monid in range(7):
            mmean=v[monid]
            mstd=v2[monid]
            csv_writer.writerow([k,monid+1,mmean,mstd])

#overall results
overallmeandict={}
overallstddict={}
overallneiblist=[]
for ovrid in range(1):
    for key,value in statedict.items():
        for v in value:
            overallneiblist.append(overalldict[v][ovrid])
        for v in value:
            overallneiblist.remove(overalldict[v][ovrid])
           
            if(len(overallneiblist)>=1):
                overallmean=round(statistics.mean(overallneiblist),2)
            else:
                overallmean=0
        
            
            if(len(overallneiblist)>1):
                overallstd=round(statistics.stdev(overallneiblist),2)
            else:
                overallstd=0
            overallneiblist.append(overalldict[v][ovrid])
            overallmeandict.setdefault(v,[]).append(overallmean)
            overallstddict.setdefault(v,[]).append(overallstd)
        overallneiblist=[]

overallmeandict = collections.OrderedDict(sorted(overallmeandict.items()))
overallstddict = collections.OrderedDict(sorted(overallstddict.items()))

with open('state-overall.csv', mode='w', newline='') as csv_file:
    csv_writer = csv.writer(csv_file)
    csv_writer.writerow(['districtid','overallid','statemean','statestdev'])
    for overaid in range(1):
        for (k,v), (k,v2) in zip(overallmeandict.items(), overallstddict.items()):
            omean=v[overaid]
            ostd=v2[overaid]
            csv_writer.writerow([k,overaid+1,omean,ostd])


