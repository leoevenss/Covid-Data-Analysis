#sorting and assigning the ids
import pandas as pd
import urllib, json
import csv 

#opening the modified json into dictionary 
with open('neighbor-districts-modified.json') as json_file: 
    data = json.load(json_file) 

#extracting the keys into a list for assigning id
data_keys=list()
for key,value in data.items():
    data_keys.append(key)

#sorting the keys
data_keys.sort()

#assigning the ids and storing into dictionary
id_dict={}
count=101
for i in data_keys:
    id_dict[count]=i
    count+=1

#writing it into a csv file
with open('neighbor-districts-modified.csv', mode='w', newline='') as csv_file:
    csv_writer = csv.writer(csv_file)
    csv_writer.writerow(['Id','District'])
    for key,value in id_dict.items():
            csv_writer.writerow([key,value])

#end of first question
