import pandas as pd
import urllib, json
import csv
import datetime
import statistics 
import collections

fields=['districtid','weekid','neighborhoodzscore','statezscore']
zsweekdata=pd.read_csv('zscore-week.csv',usecols=fields)


fields=['districtid','monthid','neighborhoodzscore','statezscore']
zsmonthdata=pd.read_csv('zscore-month.csv',usecols=fields)


fields=['districtid','overallid','neighborhoodzscore','statezscore']
zsoveralldata=pd.read_csv('zscore-overall.csv',usecols=fields)


niebourweekzscore=zsweekdata.filter(['districtid','weekid','neighborhoodzscore'],axis=1)
niebourmonthzscore=zsmonthdata.filter(['districtid','monthid','neighborhoodzscore'],axis=1)
niebouroverallzscore=zsoveralldata.filter(['districtid','overallid','neighborhoodzscore'],axis=1)

stateweekzscore=zsweekdata.filter(['districtid','weekid','statezscore'],axis=1)
statemonthzscore=zsmonthdata.filter(['districtid','monthid','statezscore'],axis=1)
stateoverallzscore=zsoveralldata.filter(['districtid','overallid','statezscore'],axis=1)

niebourweekzscore=niebourweekzscore.loc[(niebourweekzscore['neighborhoodzscore']!=0)]
niebourmonthzscore=niebourmonthzscore.loc[(niebourmonthzscore['neighborhoodzscore']!=0)]
niebouroverallzscore=niebouroverallzscore.loc[(niebouroverallzscore['neighborhoodzscore']!=0)]

stateweekzscore=stateweekzscore.loc[(stateweekzscore['statezscore']!=0)]
statemonthzscore=statemonthzscore.loc[(statemonthzscore['statezscore']!=0)]
stateoverallzscore=stateoverallzscore.loc[(stateoverallzscore['statezscore']!=0)]

nbweekhot=niebourweekzscore.sort_values(['weekid','neighborhoodzscore'],ascending=False).groupby('weekid').head(5)
nbweekcold=niebourweekzscore.sort_values(['weekid','neighborhoodzscore']).groupby('weekid').head(5)
nbmonthhot=niebourmonthzscore.sort_values(['monthid','neighborhoodzscore'],ascending=False).groupby('monthid').head(5)
nbmonthcold=niebourmonthzscore.sort_values(['monthid','neighborhoodzscore']).groupby('monthid').head(5)
nboverallhot=niebouroverallzscore.sort_values(['overallid','neighborhoodzscore'],ascending=False).groupby('overallid').head(5)
nboverallcold=niebouroverallzscore.sort_values(['overallid','neighborhoodzscore']).groupby('overallid').head(5)

sbweekhot=stateweekzscore.sort_values(['weekid','statezscore'],ascending=False).groupby('weekid').head(5)
sbweekcold=stateweekzscore.sort_values(['weekid','statezscore']).groupby('weekid').head(5)
sbmonthhot=statemonthzscore.sort_values(['monthid','statezscore'],ascending=False).groupby('monthid').head(5)
sbmonthcold=statemonthzscore.sort_values(['monthid','statezscore']).groupby('monthid').head(5)
sboverallhot=stateoverallzscore.sort_values(['overallid','statezscore'],ascending=False).groupby('overallid').head(5)
sboverallcold=stateoverallzscore.sort_values(['overallid','statezscore']).groupby('overallid').head(5)

#nboverall=niebourmonthzscore.sort_values(['overallid','neighborhoodzcore'],ascending=False)

#ls= niebourzscore.loc[(niebourzscore['neighborhoodzcore']!=0)]

#ls

#nbweekhot

#cases=list(ls.loc[(ls['weekid']==1) & (ls['neighborhoodzcore']!=0.0) ]['districtid'])

#cases



#hot week neighbour
nbhotweek=[]
nbhotweekdict={}
for weekid in range(1,26):
    nbhotweek=list(nbweekhot.loc[(nbweekhot['weekid']==weekid) ]['districtid'])
    
    
    nbhotweekdict[weekid]=nbhotweek
    nbhotweek=[]
#cold week neigbour
nbcoldweek=[]
nbcoldweekdict={}
for weekid in range(1,26):
    nbcoldweek=list(nbweekcold.loc[(nbweekcold['weekid']==weekid) ]['districtid'])
    
    
    nbcoldweekdict[weekid]=nbcoldweek
    nbcoldweek=[]
#hotweek state 
sbhotweek=[]
sbhotweekdict={}
for weekid in range(1,26):
    sbhotweek=list(sbweekhot.loc[(sbweekhot['weekid']==weekid) ]['districtid'])
    
    if(len(sbhotweek)>=5):
        sbhotweekdict[weekid]=sbhotweek
    else:
        sbhotweekdict[weekid]=['-','-','-','-','-']
    
    sbhotweek=[]
#cold week state
sbcoldweek=[]
sbcoldweekdict={}
for weekid in range(1,26):
    sbcoldweek=list(sbweekcold.loc[(sbweekcold['weekid']==weekid) ]['districtid'])
    
    if(len(sbcoldweek)>=5):
        sbcoldweekdict[weekid]=sbcoldweek
    else:
        sbcoldweekdict[weekid]=['-','-','-','-','-']
    sbcoldweek=[]

#sbhotweekdict


with open('top-week.csv', mode='w', newline='') as csv_file:
    csv_writer = csv.writer(csv_file)
    csv_writer.writerow(['weekid','method','spot','districtid1','districtid2','districtid3','districtid4','districtid5'])
    for wkd in range(1,26):
    
        csv_writer.writerow([wkd,'neighborhood','hot',nbhotweekdict[wkd][0],nbhotweekdict[wkd][1],nbhotweekdict[wkd][2],nbhotweekdict[wkd][3],nbhotweekdict[wkd][4]])
        csv_writer.writerow([wkd,'neighborhood','cold',nbcoldweekdict[wkd][0],nbcoldweekdict[wkd][1],nbcoldweekdict[wkd][2],nbcoldweekdict[wkd][3],nbcoldweekdict[wkd][4]])
        csv_writer.writerow([wkd,'state','hot',sbhotweekdict[wkd][0],sbhotweekdict[wkd][1],sbhotweekdict[wkd][2],sbhotweekdict[wkd][3],sbhotweekdict[wkd][4]])
        csv_writer.writerow([wkd,'state','cold',sbcoldweekdict[wkd][0],sbcoldweekdict[wkd][1],sbcoldweekdict[wkd][2],sbcoldweekdict[wkd][3],sbcoldweekdict[wkd][4]])



#hot month neighbour
nbhotmonth=[]
nbhotmonthdict={}
for monthid in range(1,8):
    nbhotmonth=list(nbmonthhot.loc[(nbmonthhot['monthid']==monthid) ]['districtid'])
    
    
    nbhotmonthdict[monthid]=nbhotmonth
    nbhotmonth=[]
#cold month neigbour
nbcoldmonth=[]
nbcoldmonthdict={}
for monthid in range(1,8):
    nbcoldmonth=list(nbmonthcold.loc[(nbmonthcold['monthid']==monthid) ]['districtid'])
    
    
    nbcoldmonthdict[monthid]=nbcoldmonth
    nbcoldmonth=[]
#hotmonth state 
sbhotmonth=[]
sbhotmonthdict={}
for monthid in range(1,8):
    sbhotmonth=list(sbmonthhot.loc[(sbmonthhot['monthid']==monthid) ]['districtid'])
    
    if(len(sbhotmonth)>=5):
        sbhotmonthdict[monthid]=sbhotmonth
    else:
        sbhotmonthdict[monthid]=['-','-','-','-','-']
    
    sbhotmonth=[]
#cold month state
sbcoldmonth=[]
sbcoldmonthdict={}
for monthid in range(1,8):
    sbcoldmonth=list(sbmonthcold.loc[(sbmonthcold['monthid']==monthid) ]['districtid'])
    
    if(len(sbcoldmonth)>=5):
        sbcoldmonthdict[monthid]=sbcoldmonth
    else:
        sbcoldmonthdict[monthid]=['-','-','-','-','-']
    sbcoldmonth=[]

#sbcoldmonthdict

#sbhotmonthdict

#nbhotmonthdict

#nbcoldmonthdict

with open('top-month.csv', mode='w', newline='') as csv_file:
    csv_writer = csv.writer(csv_file)
    csv_writer.writerow(['monthid','method','spot','districtid1','districtid2','districtid3','districtid4','districtid5'])
    for wkd in range(1,8):
    
        csv_writer.writerow([wkd,'neighborhood','hot',nbhotmonthdict[wkd][0],nbhotmonthdict[wkd][1],nbhotmonthdict[wkd][2],nbhotmonthdict[wkd][3],nbhotmonthdict[wkd][4]])
        csv_writer.writerow([wkd,'neighborhood','cold',nbcoldmonthdict[wkd][0],nbcoldmonthdict[wkd][1],nbcoldmonthdict[wkd][2],nbcoldmonthdict[wkd][3],nbcoldmonthdict[wkd][4]])
        csv_writer.writerow([wkd,'state','hot',sbhotmonthdict[wkd][0],sbhotmonthdict[wkd][1],sbhotmonthdict[wkd][2],sbhotmonthdict[wkd][3],sbhotmonthdict[wkd][4]])
        csv_writer.writerow([wkd,'state','cold',sbcoldmonthdict[wkd][0],sbcoldmonthdict[wkd][1],sbcoldmonthdict[wkd][2],sbcoldmonthdict[wkd][3],sbcoldmonthdict[wkd][4]])





#hot overall neighbour
nbhotoverall=[]
nbhotoveralldict={}
for overallid in range(1,2):
    nbhotoverall=list(nboverallhot.loc[(nboverallhot['overallid']==overallid) ]['districtid'])
    
    
    nbhotoveralldict[overallid]=nbhotoverall
    nbhotoverall=[]
#cold month neigbour
nbcoldoverall=[]
nbcoldoveralldict={}
for overallid in range(1,2):
    nbcoldoverall=list(nboverallcold.loc[(nboverallcold['overallid']==overallid) ]['districtid'])
    
    
    nbcoldoveralldict[overallid]=nbcoldoverall
    nbcoldoverall=[]
#hotmonth state 
sbhotoverall=[]
sbhotoveralldict={}
for overallid in range(1,2):
    sbhotoverall=list(sboverallhot.loc[(sboverallhot['overallid']==overallid) ]['districtid'])
    
    #if(len(sbhotoverall)>=5):
    sbhotoveralldict[overallid]=sbhotoverall
    #else:
     #   sbhotmonthdict[overallid]=['-','-','-','-','-']
    
    sbhotoverall=[]
#cold month state
sbcoldoverall=[]
sbcoldoveralldict={}
for overallid in range(1,2):
    sbcoldoverall=list(sboverallcold.loc[(sboverallcold['overallid']==overallid) ]['districtid'])
    
    #if(len(sbcoldmonth)>=5):
    sbcoldoveralldict[overallid]=sbcoldoverall
    #else:
     #   sbcoldmonthdict[overallid]=['-','-','-','-','-']
    sbcoldoverall=[]

#sbhotoveralldict

with open('top-overall.csv', mode='w', newline='') as csv_file:
    csv_writer = csv.writer(csv_file)
    csv_writer.writerow(['overallid','method','spot','districtid1','districtid2','districtid3','districtid4','districtid5'])
    for wkd in range(1,2):
    
        csv_writer.writerow([wkd,'neighborhood','hot',nbhotoveralldict[wkd][0],nbhotoveralldict[wkd][1],nbhotoveralldict[wkd][2],nbhotoveralldict[wkd][3],nbhotoveralldict[wkd][4]])
        csv_writer.writerow([wkd,'neighborhood','cold',nbcoldoveralldict[wkd][0],nbcoldoveralldict[wkd][1],nbcoldoveralldict[wkd][2],nbcoldoveralldict[wkd][3],nbcoldoveralldict[wkd][4]])
        csv_writer.writerow([wkd,'state','hot',sbhotoveralldict[wkd][0],sbhotoveralldict[wkd][1],sbhotoveralldict[wkd][2],sbhotoveralldict[wkd][3],sbhotoveralldict[wkd][4]])
        csv_writer.writerow([wkd,'state','cold',sbcoldoveralldict[wkd][0],sbcoldoveralldict[wkd][1],sbcoldoveralldict[wkd][2],sbcoldoveralldict[wkd][3],sbcoldoveralldict[wkd][4]])












