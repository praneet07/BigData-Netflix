"""
Requests customer id, connects to mongodb to retrieve the data and call the item based collaborative filtering algorithm
"""

import sys
import pandas as pd
import pymongo as py
from pymongo import MongoClient
from math import sqrt


__author__="Apoorva Garlanka"


"""
Import MongoClient from pymongo adn use MongoClient to create a connection.If you do not
specify any arguments to MongoClient, then MongoClient defaults to the MongoDB instance
that runs on the localhost interface on port 27017.
"""


client = MongoClient()

#Assigning the database named data to the local variable db

db=client['data']

#Assigning the collection object to a variable for use anywhere in the program

coll = db['netflix']




#Import sys to take input from the system and saving it in a variable

Cust_Id = input("Enter Customer ID:")

#Querying the data in mongodb in python through pymongo

cursor1= db.sample.find({ "Customer_Reveiws.CustID":Cust_Id},{"Customer_Reveiws.ReviewMonth" :0
,"Customer_Reveiws.ReviewDay" : 0,"Customer_Reveiws.ReviewYear" : 0,"MovieType":0,})

#Converting the list obtained from the query into a data frame

result1= pd.DataFrame(list(cursor1))
result1

#Formatting the data frame so as to fit the the algorithm
Frames1 = []
for i in range(result1.shape[0]):
    temp1 = pd.DataFrame(result1.iloc[i,0])
    temp1['Director'] = result1.iloc[i,1]
    temp1['Genre'] = ','.join(result1.iloc[i,2])
    temp1['NetflixID'] = result1.iloc[i,3]
    temp1['Production_Year'] = result1.iloc[i,4]
    temp1['Title'] = result1.iloc[i,5]
    #temp = pd.concat(temp)
    Frames1.append(temp1)

Frames1= pd.concat(Frames1)

#Retrieving the movie and rating given by a particular Customer,which is specified by the user

Frames1 = Frames1.loc[Frames1['CustID']== Cust_Id]
Frames1= Frames1[["NetflixID","UserRating"]]
Cust_Id = input("Enter Customer ID:")

#Converting into a dictionary

d2=Frames1.set_index("NetflixID")["UserRating"].to_dict()

#Query to retrieve all the data to find out the similarity matrix
cursor = db.netflix.find()
result=pd.DataFrame(list(cursor))
result.head()
Frames=[]
for i in range(result.shape[0]):
    temp = pd.DataFrame(result.iloc[i,0])
    temp['NetflixID'] = result.iloc[i,4]
    temp['Title'] = result.iloc[i,6]
    #temp = pd.concat(temp)
    Frames.append(temp)

Frames= pd.concat(Frames)
Frames.head()
Frames = Frames[['CustID','UserRating','NetflixID']]
Frames.head()
temp1=Frames.values.tolist()

#Getting the data into a dictionary format
d1={}
dict2={}
key=temp1[0][2]
for i in range(len(temp1)):
    if(key!=temp1[i][2]):
        d1[key]=dict2
        key=temp1[i][2]
        dict2={}

    dict2[temp1[i][0]]=temp1[i][1]
cd1={}
for i in d1:
    temp={}
    for j in d1[i].items():
        temp[int(j[0])]=j[1]
    cd1[int(i)]=temp
cd2={}
for i in d2.items():
    cd2[int(i[0])]=float(i[1])

#Calling the function authored by Satvik Shetty
simmat=similarity_matrix(cd1)
recs=recommendation(cd2,cd1,simmat,Cust_Id)


#Retrieving the title from the movie movie ID and displaying it with the simmilarity score
a=[]
for j in recs:
    for i in range(len(result['Netflix'])):
        if(j[1] == result['Netflix'][i]):
              a.append((j[0],result['Title'][i]))