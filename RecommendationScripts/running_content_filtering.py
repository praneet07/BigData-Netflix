"""
Connects to mongodb to retrieve data and call the content filtering algorithm
"""

import sys
import pandas as pd
import pymongo as py
from pymongo import MongoClient
import operator
from operator import itemgetter


__author__="Apoorva Garlanka"

#Connected python to mongodb
client = MongoClient()
db=client['data']
#Query
cursor = db.netflix.find()
result=pd.DataFrame(list(cursor))
result.head()

#Converting the result obtained to a format required for the algorithm
result = result.drop(['Production_Year','_id'], axis=1)
result.head()
result = result[['Director','Genre','MovieType','NetflixID','Title']]
data =result.values.tolist()
data
type(movie[3])
mid = input("enter movie id:")

#Function by Saurav Chakroborthy

#Converted results into dataframe
df = pd.DataFrame(res)