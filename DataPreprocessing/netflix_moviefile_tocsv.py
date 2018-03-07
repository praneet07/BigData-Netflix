"""
To extract data from netflix movie file in txt format and save in csv format
"""
import csv

__author__="Satvik Shetty"

#read data from txt file
netflixtitle=[line.strip() for line in open("movie_titles.txt","r")]

#write to csv
with open("movietitle.csv","w", newline='') as f:
    writer=csv.writer(f)
    for item in netflixtitle:
        data=item.split(",")
        #Handle movie titles that have one or more commas in their name
        if(len(data)>3):
            if(len(data)==4):
                merge=data[2]+","+data[3]
            elif(len(data)==5):
                merge=data[2]+","+data[3]+","+data[4]
            else:
                merge=data[2]+","+data[3]+","+data[4]+","+data[5]
            data=[data[0],data[1],merge]
        writer.writerow(data)

