import pandas as pd
import urllib, json
import csv
import datetime
import statistics 
import collections

#weekwise
fields=['districtid','weekid','cases']
weekdata=pd.read_csv('cases-week.csv',usecols=fields)


weekcaselist=[]
weekdict={}
for i in range(101,728):
    for weekid in range(1,26):
        cases=int(weekdata.loc[(weekdata['weekid']==weekid) & (weekdata['districtid']==int(i)) ]['cases'])
        weekcaselist.append(cases)
    
    weekdict[i]=weekcaselist
    weekcaselist=[]



fields=['districtid','monthid','cases']
monthdata=pd.read_csv('cases-month.csv',usecols=fields)


monthcaselist=[]
monthdict={}
for i in range(101,728):
    for monthid in range(1,8):
        cases=int(monthdata.loc[(monthdata['monthid']==monthid) & (monthdata['districtid']==int(i)) ]['cases'])
        monthcaselist.append(cases)
    
    monthdict[i]=monthcaselist
    monthcaselist=[]

#len(monthdict[101])

fields=['districtid','overallid','cases']
overalldata=pd.read_csv('cases-overall.csv',usecols=fields)


overallcaselist=[]
overalldict={}
for i in range(101,728):
    
    cases=int(overalldata.loc[(overalldata['overallid']==1) & (overalldata['districtid']==int(i)) ]['cases'])
    overallcaselist.append(cases)
    
    overalldict[i]=overallcaselist
    overallcaselist=[]

#len(overalldict[101])



#weekneigbour
fields=['districtid','weekid','neighbormean','neighborstdev']
neighborweekdata=pd.read_csv('neighbor-week.csv',usecols=fields)


nwmeanlist=[]
nwmeanweekdict={}
for i in range(101,728):
    for weekid in range(1,26):
        cases=float(neighborweekdata.loc[(neighborweekdata['weekid']==weekid) & (neighborweekdata['districtid']==int(i)) ]['neighbormean'])
        nwmeanlist.append(cases)
    
    nwmeanweekdict[i]=nwmeanlist
    nwmeanlist=[]

#nwmeanweekdict

nwstdlist=[]
nwstdweekdict={}
for i in range(101,728):
    for weekid in range(1,26):
        cases=float(neighborweekdata.loc[(neighborweekdata['weekid']==weekid) & (neighborweekdata['districtid']==int(i)) ]['neighborstdev'])
        nwstdlist.append(cases)
    
    nwstdweekdict[i]=nwstdlist
    nwstdlist=[]

#nwstdweekdict



nwzscoreweekdata={}
for weekid in range(25):
    for (k,v1),(k,v2),(k,v3) in zip(weekdict.items(),nwmeanweekdict.items(),nwstdweekdict.items()):
        if v3[weekid]==0.0:
            nwzscoreweekdata.setdefault(k,[]).append(0.0)
        else:
            
            nwzscoreweekdata.setdefault(k,[]).append(round((v1[weekid]-v2[weekid])/v3[weekid],2))

#nwzscoreweekdata

fields=['districtid','weekid','statemean','statestdev']
stateweekdata=pd.read_csv('state-week.csv',usecols=fields)


swmeanlist=[]
swmeanweekdict={}
for i in range(101,728):
    for weekid in range(1,26):
        cases=float(stateweekdata.loc[(stateweekdata['weekid']==weekid) & (stateweekdata['districtid']==int(i)) ]['statemean'])
        swmeanlist.append(cases)
    
    swmeanweekdict[i]=swmeanlist
    swmeanlist=[]

#swmeanweekdict

swstdlist=[]
swstdweekdict={}
for i in range(101,728):
    for weekid in range(1,26):
        cases=float(stateweekdata.loc[(stateweekdata['weekid']==weekid) & (stateweekdata['districtid']==int(i)) ]['statestdev'])
        swstdlist.append(cases)
    
    swstdweekdict[i]=swstdlist
    swstdlist=[]

swzscorestateweekdata={}
for weekid in range(25):
    for (k,v1),(k,v2),(k,v3) in zip(weekdict.items(),swmeanweekdict.items(),swstdweekdict.items()):
        if v3[weekid]==0.0:
            swzscorestateweekdata.setdefault(k,[]).append(0.0)
        else:
            swzscorestateweekdata.setdefault(k,[]).append(round((v1[weekid]-v2[weekid])/v3[weekid],2))

#creating week zscore csv
nwzscoreweekdata = collections.OrderedDict(sorted(nwzscoreweekdata.items()))

swzscorestateweekdata = collections.OrderedDict(sorted(swzscorestateweekdata.items()))



with open('zscore-week.csv', mode='a', newline='') as csv_file:
    csv_writer = csv.writer(csv_file)
    csv_writer.writerow(['districtid','weekid','neighborhoodzscore','statezscore'])
    
    for (k,v), (k,v2) in zip(nwzscoreweekdata.items(), swzscorestateweekdata.items()):
            #for (nv,sv) in zip(v,v2):
            for weekid in range(25):
                nwzs=v[weekid]
                swzs=v2[weekid]
                csv_writer.writerow([k,weekid+1,nwzs,swzs])









##Creating month wise

fields=['districtid','monthid','neighbormean','neighborstdev']
neighbormonthdata=pd.read_csv('neighbor-month.csv',usecols=fields)


nmmeanlist=[]
nmmeanmonthdict={}
for i in range(101,728):
    for monthid in range(1,8):
        cases=float(neighbormonthdata.loc[(neighbormonthdata['monthid']==monthid) & (neighbormonthdata['districtid']==int(i)) ]['neighbormean'])
        nmmeanlist.append(cases)
    
    nmmeanmonthdict[i]=nmmeanlist
    nmmeanlist=[]

#nmmeanmonthdict

nmstdlist=[]
nmstdmonthdict={}
for i in range(101,728):
    for monthid in range(1,8):
        cases=float(neighbormonthdata.loc[(neighbormonthdata['monthid']==monthid) & (neighbormonthdata['districtid']==int(i)) ]['neighborstdev'])
        nmstdlist.append(cases)
    
    nmstdmonthdict[i]=nmstdlist
    nmstdlist=[]

#nmstdmonthdict

nmzscoremonthdata={}
for monid in range(7):
    for (k,v1),(k,v2),(k,v3) in zip(monthdict.items(),nmmeanmonthdict.items(),nmstdmonthdict.items()):
        if v3[monid]==0.0:
            nmzscoremonthdata.setdefault(k,[]).append(0.0)
        else:
            nmzscoremonthdata.setdefault(k,[]).append(round((v1[monid]-v2[monid])/v3[monid],2))
        

#nmzscoremonthdata

fields=['districtid','monthid','statemean','statestdev']
statemonthdata=pd.read_csv('state-month.csv',usecols=fields)


smmeanlist=[]
smmeanmonthdict={}
for i in range(101,728):
    for monthid in range(1,8):
        cases=float(statemonthdata.loc[(statemonthdata['monthid']==monthid) & (statemonthdata['districtid']==int(i)) ]['statemean'])
        smmeanlist.append(cases)
    
    smmeanmonthdict[i]=smmeanlist
    smmeanlist=[]

smstdlist=[]
smstdmonthdict={}
for i in range(101,728):
    for monthid in range(1,8):
        cases=float(statemonthdata.loc[(statemonthdata['monthid']==monthid) & (statemonthdata['districtid']==int(i)) ]['statestdev'])
        smstdlist.append(cases)
    
    smstdmonthdict[i]=smstdlist
    smstdlist=[]

smzscorestatemonthdata={}
for monid in range(7):
    for (k,v1),(k,v2),(k,v3) in zip(monthdict.items(),smmeanmonthdict.items(),smstdmonthdict.items()):
        if v3[monid]==0.0:
            smzscorestatemonthdata.setdefault(k,[]).append(0.0)
        else:
            smzscorestatemonthdata.setdefault(k,[]).append(round((v1[monid]-v2[monid])/v3[monid],2))

#creatin zscore csv
nmzscoremonthdata = collections.OrderedDict(sorted(nmzscoremonthdata.items()))

smzscorestatemonthdata = collections.OrderedDict(sorted(smzscorestatemonthdata.items()))



#smzscorestatemonthdata

with open('zscore-month.csv', mode='a', newline='') as csv_file:
    csv_writer = csv.writer(csv_file)
    csv_writer.writerow(['districtid','monthid','neighborhoodzscore','statezscore'])

    for (k,v), (k,v2) in zip(nmzscoremonthdata.items(), smzscorestatemonthdata.items()):
        for monthid in range(7):
            nmzs=v[monthid]
            smzs=v2[monthid]
            csv_writer.writerow([k,monthid+1,nmzs,smzs])

fields=['districtid','overallid','neighbormean','neighborstdev']
neighboroveralldata=pd.read_csv('neighbor-overall.csv',usecols=fields)


nomeanlist=[]
nomeanoveralldict={}
for i in range(101,728):
    
    cases=float(neighboroveralldata.loc[(neighboroveralldata['overallid']==1) & (neighboroveralldata['districtid']==int(i)) ]['neighbormean'])
    nomeanlist.append(cases)
    
    nomeanoveralldict[i]=nomeanlist
    nomeanlist=[]

nostdlist=[]
nostdoveralldict={}
for i in range(101,728):
    
    cases=float(neighboroveralldata.loc[(neighboroveralldata['overallid']==1) & (neighboroveralldata['districtid']==int(i)) ]['neighborstdev'])
    nostdlist.append(cases)
    
    nostdoveralldict[i]=nostdlist
    nostdlist=[]

    nozscoreoveralldata={}

    for (k,v1),(k,v2),(k,v3) in zip(overalldict.items(),nomeanoveralldict.items(),nostdoveralldict.items()):
        if v3[0]==0.0:
            nozscoreoveralldata[k]=0.0
        else:
            nozscoreoveralldata[k]=round((v1[0]-v2[0])/v3[0],2)



fields=['districtid','overallid','statemean','statestdev']
stateoveralldata=pd.read_csv('state-overall.csv',usecols=fields)


someanlist=[]
someanoveralldict={}
for i in range(101,728):
    
    cases=float(stateoveralldata.loc[(stateoveralldata['overallid']==1) & (stateoveralldata['districtid']==int(i)) ]['statemean'])
    someanlist.append(cases)
    
    someanoveralldict[i]=someanlist
    someanlist=[]

sostdlist=[]
sostdoveralldict={}
for i in range(101,728):
    
    cases=float(stateoveralldata.loc[(stateoveralldata['overallid']==1) & (stateoveralldata['districtid']==int(i)) ]['statestdev'])
    sostdlist.append(cases)
    
    sostdoveralldict[i]=sostdlist
    sostdlist=[]

sozscorestateoveralldata={}

for (k,v1),(k,v2),(k,v3) in zip(overalldict.items(),someanoveralldict.items(),sostdoveralldict.items()):
    if v3[0]==0.0:
        sozscorestateoveralldata[k]=0.0
    else:
        sozscorestateoveralldata[k]=round((v1[0]-v2[0])/v3[0],2)

#creatin zscore csv
nozscoreoveralldata = collections.OrderedDict(sorted(nozscoreoveralldata.items()))

sozscorestateoveralldata = collections.OrderedDict(sorted(sozscorestateoveralldata.items()))



#sozscorestateoveralldata

with open('zscore-overall.csv', mode='a', newline='') as csv_file:
    csv_writer = csv.writer(csv_file)
    csv_writer.writerow(['districtid','overallid','neighborhoodzscore','statezscore'])
    
    for (k,v), (k,v2) in zip(nozscoreoveralldata.items(), sozscorestateoveralldata.items()):
        nozs=v
        sozs=v2
        csv_writer.writerow([k,1,nozs,sozs])




