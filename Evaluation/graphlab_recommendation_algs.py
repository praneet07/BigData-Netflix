"""
Runs the recommendation algorithm from graphlabs on the sample datatset
"""

import os
import graphlab as gl

__author__="Apoorva Garlanka"

sf = gl.SFrame("/Users/apoorvashankar/Desktop/Spring 2016/Big Data Analytics/project/sample.csv")
sf.head()

#Create a recommender that uses item-item similarities based on users in common.

m=gl.recommender.create(sf, target='Rating')
recs = m.recommend()
recs