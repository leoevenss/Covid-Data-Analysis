#starting with question2
import pandas as pd
import urllib, json
import csv
import datetime


#reading data from data-all.json
alldata=pd.read_json('data-all.json')

visualisedata=alldata.reset_index()



#extracting the states into a list
state_list=list(visualisedata['index'])

#removing TT and UN
state_list.remove('TT')
state_list.remove('UN')



#extracting all districts statewise into a dictionary with state as key
alldistricts=dict()
for date in alldata.keys():
    for state in alldata[date].keys():
            if alldata[date][state]==alldata[date][state]:
                if 'districts' in alldata[date][state].keys():
                        for distr in alldata[date][state]['districts']:
                            if distr!='Unknown':
                                alldistricts.setdefault(state,[]).append(distr)
                                                            
                        

#removing duplicate district lists
for key,value in alldistricts.items():
    alldistricts[key]=set(value)

#rename the districts with same name with state code at end
alldistricts['BR'].remove('Aurangabad')
alldistricts['BR'].add('Aurangabadbr')
alldistricts['MH'].remove('Aurangabad')
alldistricts['MH'].add('Aurangabadmh')

alldistricts['CT'].remove('Balrampur')
alldistricts['CT'].add('Balrampurct')
alldistricts['UP'].remove('Balrampur')
alldistricts['UP'].add('Balrampurup')

alldistricts['RJ'].remove('Pratapgarh')
alldistricts['RJ'].add('Pratapgarhrj')
alldistricts['UP'].remove('Pratapgarh')
alldistricts['UP'].add('Pratapgarhup')

alldistricts['CT'].remove('Bilaspur')
alldistricts['CT'].add('Bilaspurct')
alldistricts['HP'].remove('Bilaspur')
alldistricts['HP'].add('Bilaspurhp')

alldistricts['HP'].remove('Hamirpur')
alldistricts['HP'].add('Hamirpurhp')
alldistricts['UP'].remove('Hamirpur')
alldistricts['UP'].add('Hamirpurup')



#reading the modified file so as to get the ids
fields=['Id','District']
mapdata=pd.read_csv('neighbor-districts-modified.csv',usecols=fields)

#converting dataframe to dictionary
mapdict=mapdata.to_dict('Id')

#creating dictionary with district name as key and id as value
dnamedict={}        
for key,value in mapdict.items():
        dnamedict[value['District'].split("/")[0]]=value['Id']
            



#getting states from alldistricts
statecodes=[]
for key, val in alldistricts.items():
    statecodes.append(key)

#getting the dates into a list
alldates=[]    
for date in alldata.keys():
    alldates.append(date)

#interval of dates
start=datetime.datetime(2020, 3, 15)
end=datetime.datetime(2020, 9, 5)

#refining our dateinterval
daterange=[]
for i in alldates:
    if i>=start and i<=end:
        daterange.append(i)
    

#writing all data into an excel file


#extracting district data from all-data
with open('alldata_base.csv', mode='a', newline='') as csv_file:
    csv_writer = csv.writer(csv_file)
    csv_writer.writerow(['Date','State','District','Cases'])
        
    for state in statecodes:
        for dist in alldistricts[state]:
            temp=dist
            for date in daterange:
                if dist.lower() in dnamedict.keys():
                    num=dnamedict[dist.lower()]
                    if state=='BR' and dist=='Aurangabadbr':
                        temp=str('Aurangabad')
                    elif state=='MH' and dist=='Aurangabadmh':                    
                        temp=str('Aurangabad')
                    elif state=='CT' and dist=='Balrampurct':
                        temp=str('Balrampur')
                    elif state=='UP' and dist=='Balrampurup':
                        temp=str('Balrampur')
                    elif state=='RJ' and dist=='Pratapgarhrj':
                        temp=str('Pratapgarh')
                    elif state=='UP' and dist=='Pratapgarhup':
                        temp=str('Pratapgarh')
                    elif state=='CT' and dist=='Bilaspurct':
                        temp=str('Bilaspur')
                    elif state=='HP' and dist=='Bilaspurhp':
                        temp=str('Bilaspur')
                    elif state=='HP' and dist=='Hamirpurhp':
                        temp=str('Hamirpur')
                    elif state=='UP' and dist=='Hamirpurup':
                        temp=str('Hamirpur')
                    try:
                        if state in alldata[date].keys():

                                if "districts" in alldata[date][state].keys():

                                        if temp in alldata[date][state]['districts'].keys():
                                            if 'delta' in alldata[date][state]['districts'][temp].keys():
                                                if 'confirmed'in alldata[date][state]['districts'][temp]['delta'].keys():
                                                    result=alldata[date][state]['districts'][temp]['delta']['confirmed']
                                                    csv_writer.writerow([date,state,num,result])

                                                else:
                                                    csv_writer.writerow([date,state,num,0])

                                            else:
                                                csv_writer.writerow([date,state,num,0])

                                        else:
                                            csv_writer.writerow([date,state,num,0])

                                else:
                                    csv_writer.writerow([date,state,num,0])


                        else:
                            csv_writer.writerow([date,state,num,0])
                    except:
                        csv_writer.writerow([date,state,num,0])

#extracting data for merged districts
with open('alldata_base.csv', mode='a', newline='') as csv_file:
    csv_writer = csv.writer(csv_file)
    
        
    for state in ['TG','SK','MN','GA','AS']:
            if state=='TG':
                num=665
            elif state=='SK':
                num=628
            elif state=='MN':
                num=469
            elif state=='GA':
                num=303
            elif state=='AS':
                num=132
            
            for date in daterange:
                    try:
                        if state in alldata[date].keys():

                                #if "districts" in data[date][state].keys():

                                        #if 'Unknown' in data[date][state]['districts'].keys():
                                            if 'delta' in alldata[date][state].keys():
                                                if 'confirmed'in alldata[date][state]['delta'].keys():
                                                    result=alldata[date][state]['delta']['confirmed']
                                                    csv_writer.writerow([date,state,num,result])

                                                else:
                                                    csv_writer.writerow([date,state,num,0])

                                            else:
                                                csv_writer.writerow([date,state,num,0])

                                        #else:
                                         #   csv_writer.writerow([date,state,num,0])

                                #else:
                                #    csv_writer.writerow([date,state,num,0])


                        else:
                            csv_writer.writerow([date,state,num,0])
                    except:
                        csv_writer.writerow([date,state,num,0])


