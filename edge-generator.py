import pandas as pd
import urllib, json
import csv 

with open('neighbor-districts-modified.json') as json_file: 
    data = json.load(json_file)

with open('neighbor-districts-modified.csv', mode='r') as infile:
    reader = csv.reader(infile)
    mydict = {rows[1]:rows[0] for rows in reader}

#deleting the first row
del mydict['District']



templist=[]
for key,value in data.items():
    for val in value:
        if(mydict[key]<=mydict[val]):
            templist.append([mydict[key],mydict[val]])
        else:
            templist.append([mydict[val],mydict[key]])



unique_list=[]
for x in templist: 
        # check if exists in unique_list or not 
        if x not in unique_list: 
            unique_list.append(x) 

unique_list.sort()

#unique_list

with open('edge-graph.csv', mode='w', newline='') as csv_file:
    csv_writer = csv.writer(csv_file)
    csv_writer.writerow(['districti','districtj'])
    for value in unique_list:
        csv_writer.writerow([value[0],value[1]])
