import pandas as pd
import urllib, json
import csv
import datetime
import statistics 
import collections

#get weekly cases

fields=['districtid','weekid','cases']
weekdata=pd.read_csv('cases-week.csv',usecols=fields)


caselist=[]
weekdict={}
for i in range(101,728):
    for weekid in range(1,26):
        cases=int(weekdata.loc[(weekdata['weekid']==weekid) & (weekdata['districtid']==int(i)) ]['cases'])
        caselist.append(cases)
    
    weekdict[i]=caselist
    caselist=[]

#get neibor values

fields=['districtid','weekid','neighbormean','neighborstdev']
neighbordata=pd.read_csv('neighbor-week.csv',usecols=fields)


#neigbour mean
nmeanlist=[]
nmeanweekdict={}
for i in range(101,728):
    for weekid in range(1,26):
        cases=float(neighbordata.loc[(neighbordata['weekid']==weekid) & (neighbordata['districtid']==int(i)) ]['neighbormean'])
        nmeanlist.append(cases)
    
    nmeanweekdict[i]=nmeanlist
    nmeanlist=[]



#neigbor std
nstdlist=[]
nstdweekdict={}
for i in range(101,728):
    for weekid in range(1,26):
        cases=float(neighbordata.loc[(neighbordata['weekid']==weekid) & (neighbordata['districtid']==int(i)) ]['neighborstdev'])
        nstdlist.append(cases)
    
    nstdweekdict[i]=nstdlist
    nstdlist=[]

#get state values

fields=['districtid','weekid','statemean','statestdev']
statedata=pd.read_csv('state-week.csv',usecols=fields)


#state mean
smeanlist=[]
smeanweekdict={}
for i in range(101,728):
    for weekid in range(1,26):
        cases=float(statedata.loc[(statedata['weekid']==weekid) & (statedata['districtid']==int(i)) ]['statemean'])
        smeanlist.append(cases)
    
    smeanweekdict[i]=smeanlist
    smeanlist=[]



#state std
sstdlist=[]
sstdweekdict={}
for i in range(101,728):
    for weekid in range(1,26):
        cases=float(statedata.loc[(statedata['weekid']==weekid) & (statedata['districtid']==int(i)) ]['statestdev'])
        sstdlist.append(cases)
    
    sstdweekdict[i]=sstdlist
    sstdlist=[]

#actual logic

#creatin zscore csv
weekdict = collections.OrderedDict(sorted(weekdict.items()))
nmeanweekdict = collections.OrderedDict(sorted(nmeanweekdict.items()))
nstdweekdict = collections.OrderedDict(sorted(nstdweekdict.items()))
smeanweekdict = collections.OrderedDict(sorted(smeanweekdict.items()))
sstdweekdict = collections.OrderedDict(sorted(sstdweekdict.items()))



#len(sstdweekdict[101])

nhspwk=dict()
ncspwk=dict()
shspwk=dict()
scspwk=dict()
for (k,wkc),(k,nm),(k,ns),(k,sm),(k,ss) in zip(weekdict.items(),nmeanweekdict.items(),nstdweekdict.items(),smeanweekdict.items(),sstdweekdict.items()):
    for weekid in range(25):
        if wkc[weekid]>(nm[weekid]+ns[weekid]):
            nhspwk.setdefault(weekid,[]).append(k)
        if wkc[weekid]<(nm[weekid]-ns[weekid]):
            ncspwk.setdefault(weekid,[]).append(k)
        if wkc[weekid]>(sm[weekid]+ss[weekid]):
            shspwk.setdefault(weekid,[]).append(k)
        if wkc[weekid]<(sm[weekid]-ss[weekid]):
            scspwk.setdefault(weekid,[]).append(k)

#write to csv file

with open('method-spot-week.csv', mode='w', newline='') as csv_file:
    csv_writer = csv.writer(csv_file)
    csv_writer.writerow(['weekid','method','spot','districtid'])

    for wkid in range(25):
        if wkid in nhspwk.keys():
            for v in nhspwk[wkid]:
                csv_writer.writerow([wkid+1,'neighborhood','hot',v])
        if wkid in ncspwk.keys():
            for v1 in ncspwk[wkid]:
                csv_writer.writerow([wkid+1,'neighborhood','cold',v1])
        if wkid in shspwk.keys():
            for v2 in shspwk[wkid]:
                csv_writer.writerow([wkid+1,'state','hot',v2])
        if wkid in scspwk.keys():
            for v3 in scspwk[wkid]:
                csv_writer.writerow([wkid+1,'state','cold',v3])







#month
fields=['districtid','monthid','cases']
monthdata=pd.read_csv('cases-month.csv',usecols=fields)


mcaselist=[]
monthdict={}
for i in range(101,728):
    for monthid in range(1,8):
        mcases=int(monthdata.loc[(monthdata['monthid']==monthid) & (monthdata['districtid']==int(i)) ]['cases'])
        mcaselist.append(mcases)
    
    monthdict[i]=mcaselist
    mcaselist=[]

fields=['districtid','monthid','neighbormean','neighborstdev']
mneighbordata=pd.read_csv('neighbor-month.csv',usecols=fields)


#neigbour mean
nmmeanlist=[]
nmmeanmonthdict={}
for i in range(101,728):
    for monthid in range(1,8):
        nmcases=float(mneighbordata.loc[(mneighbordata['monthid']==monthid) & (mneighbordata['districtid']==int(i)) ]['neighbormean'])
        nmmeanlist.append(nmcases)
    
    nmmeanmonthdict[i]=nmmeanlist
    nmmeanlist=[]

#neigbor std
nmstdlist=[]
nmstdmonthdict={}
for i in range(101,728):
    for monthid in range(1,8):
        nscases=float(mneighbordata.loc[(mneighbordata['monthid']==monthid) & (mneighbordata['districtid']==int(i)) ]['neighborstdev'])
        nmstdlist.append(nscases)
    
    nmstdmonthdict[i]=nmstdlist
    nmstdlist=[]

fields=['districtid','monthid','statemean','statestdev']
mstatedata=pd.read_csv('state-month.csv',usecols=fields)


#state mean
smmeanlist=[]
smmeanmonthdict={}
for i in range(101,728):
    for monthid in range(1,8):
        smcases=float(mstatedata.loc[(mstatedata['monthid']==monthid) & (mstatedata['districtid']==int(i)) ]['statemean'])
        smmeanlist.append(smcases)
    
    smmeanmonthdict[i]=smmeanlist
    smmeanlist=[]

#state std
smstdlist=[]
smstdmonthdict={}
for i in range(101,728):
    for month in range(1,8):
        smcases=float(mstatedata.loc[(mstatedata['monthid']==monthid) & (mstatedata['districtid']==int(i)) ]['statestdev'])
        smstdlist.append(smcases)
    
    smstdmonthdict[i]=smstdlist
    smstdlist=[]

#creatin zscore csv
monthdict = collections.OrderedDict(sorted(monthdict.items()))
nmmeanmonthdict = collections.OrderedDict(sorted(nmmeanmonthdict.items()))
nmstdmonthdict = collections.OrderedDict(sorted(nmstdmonthdict.items()))
smmeanmonthdict = collections.OrderedDict(sorted(smmeanmonthdict.items()))
smstdmonthdict = collections.OrderedDict(sorted(smstdmonthdict.items()))



nhspmn=dict()
ncspmn=dict()
shspmn=dict()
scspmn=dict()
for (k,mnc),(k,nm),(k,ns),(k,sm),(k,ss) in zip(monthdict.items(),nmmeanmonthdict.items(),nmstdmonthdict.items(),smmeanmonthdict.items(),smstdmonthdict.items()):
    for monthid in range(7):
        if mnc[monthid]>(nm[monthid]+ns[monthid]):
            nhspmn.setdefault(monthid,[]).append(k)
        if mnc[monthid]<(nm[monthid]-ns[monthid]):
            ncspmn.setdefault(monthid,[]).append(k)
        if mnc[monthid]>(sm[monthid]+ss[monthid]):
            shspmn.setdefault(monthid,[]).append(k)
        if mnc[monthid]<(sm[monthid]-ss[monthid]):
            scspmn.setdefault(monthid,[]).append(k)

with open('method-spot-month.csv', mode='w', newline='') as csv_file:
    csv_writer = csv.writer(csv_file)
    csv_writer.writerow(['monthid','method','spot','districtid'])

    for mnid in range(8):
        if mnid in nhspmn.keys():
            for v in nhspmn[mnid]:
                csv_writer.writerow([mnid+1,'neighborhood','hot',v])
        if mnid in ncspmn.keys():
            for v1 in ncspmn[mnid]:
                csv_writer.writerow([mnid+1,'neighborhood','cold',v1])
        if mnid in shspmn.keys():
            for v2 in shspmn[mnid]:
                csv_writer.writerow([mnid+1,'state','hot',v2])
        if mnid in scspmn.keys():
            for v3 in scspmn[mnid]:
                csv_writer.writerow([mnid+1,'state','cold',v3])



#overall
fields=['districtid','overallid','cases']
overalldata=pd.read_csv('cases-overall.csv',usecols=fields)


ocaselist=[]
overalldict={}
for i in range(101,728):
    
    ocases=int(overalldata.loc[(overalldata['overallid']==1) & (overalldata['districtid']==int(i)) ]['cases'])
    ocaselist.append(ocases)
    
    overalldict[i]=ocaselist
    ocaselist=[]

fields=['districtid','overallid','neighbormean','neighborstdev']
oneighbordata=pd.read_csv('neighbor-overall.csv',usecols=fields)


#neigbour mean
nomeanlist=[]
nomeanoveralldict={}
for i in range(101,728):
    
    nocases=float(oneighbordata.loc[(oneighbordata['overallid']==1) & (oneighbordata['districtid']==int(i)) ]['neighbormean'])
    nomeanlist.append(nocases)
    
    nomeanoveralldict[i]=nomeanlist
    nomeanlist=[]

#neigbor std
nostdlist=[]
nostdoveralldict={}
for i in range(101,728):
    
    noscases=float(oneighbordata.loc[(oneighbordata['overallid']==1) & (oneighbordata['districtid']==int(i)) ]['neighborstdev'])
    nostdlist.append(noscases)
    
    nostdoveralldict[i]=nostdlist
    nostdlist=[]

fields=['districtid','overallid','statemean','statestdev']
ostatedata=pd.read_csv('state-overall.csv',usecols=fields)


#state mean
someanlist=[]
someanoveralldict={}
for i in range(101,728):
    
    socases=float(ostatedata.loc[(ostatedata['overallid']==1) & (ostatedata['districtid']==int(i)) ]['statemean'])
    someanlist.append(smcases)
    
    someanoveralldict[i]=someanlist
    someanlist=[]

#state std
sostdlist=[]
sostdoveralldict={}
for i in range(101,728):
    
    socases=float(ostatedata.loc[(ostatedata['overallid']==1) & (ostatedata['districtid']==int(i)) ]['statestdev'])
    sostdlist.append(socases)
    
    sostdoveralldict[i]=sostdlist
    sostdlist=[]

#creatin zscore csv
overalldict = collections.OrderedDict(sorted(overalldict.items()))
nomeanoveralldict = collections.OrderedDict(sorted(nomeanoveralldict.items()))
nostdoveralldict = collections.OrderedDict(sorted(nostdoveralldict.items()))
someanoveralldict = collections.OrderedDict(sorted(someanoveralldict.items()))
sostdoveralldict = collections.OrderedDict(sorted(sostdoveralldict.items()))



nhspo=dict()
ncspo=dict()
shspo=dict()
scspo=dict()
for (k,oc),(k,nm),(k,ns),(k,sm),(k,ss) in zip(overalldict.items(),nomeanoveralldict.items(),nostdoveralldict.items(),someanoveralldict.items(),sostdoveralldict.items()):
    for overallid in range(1):
        if oc[overallid]>(nm[overallid]+ns[overallid]):
            nhspo.setdefault(overallid,[]).append(k)
        if oc[overallid]<(nm[overallid]-ns[overallid]):
            ncspo.setdefault(overallid,[]).append(k)
        if oc[overallid]>(sm[overallid]+ss[overallid]):
            shspo.setdefault(overallid,[]).append(k)
        if oc[overallid]<(sm[overallid]-ss[overallid]):
            scspo.setdefault(overallid,[]).append(k)

with open('method-spot-overall.csv', mode='w', newline='') as csv_file:
    csv_writer = csv.writer(csv_file)
    csv_writer.writerow(['overallid','method','spot','districtid'])

    for oid in range(1):
        if oid in nhspo.keys():
            for v in nhspo[oid]:
                csv_writer.writerow([oid+1,'neighborhood','hot',v])
        if oid in ncspo.keys():
            for v1 in ncspo[oid]:
                csv_writer.writerow([oid+1,'neighborhood','cold',v1])
        if oid in shspo.keys():
            for v2 in shspo[oid]:
                csv_writer.writerow([oid+1,'state','hot',v2])
        if oid in scspo.keys():
            for v3 in scspo[oid]:
                csv_writer.writerow([oid+1,'state','cold',v3])


