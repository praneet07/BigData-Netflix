"""
Match the netflixIDs to IMDbIDs from the title table of imdb
"""

#! /usr/bin/env python
import MySQLdb,csv

__author__="Satvik Shetty"

#establish DB connection to retrieve IMDb data
string = "************"     #change this to yours
password = "************"    #change this to yours
db_con = MySQLdb.connect(host="db.soic.indiana.edu", port = 3306, user=string, passwd=password, db=string)
cursor = db_con.cursor()

#Keep a count of entries matches, entries with no match and entries with multiple matches
count_s=0
count_m=0
count_e=0

#Read from the netflix movie title file
NetflixRow=[line for line in csv.reader(open("movietitle.csv","r"))]
#write to a new csv
with open("imdb_link.csv","w") as f:
    writer=csv.writer(f)
    SQL=""
    for data in NetflixRow:
        try:
            # Handling movie titles which have symbols " and ' in movie name
            if '"' in data[2]:
                SQL = "SELECT * FROM title where title='"+data[2]+"' and production_year='"+data[1]+"' and kind_id not in (6,7);"
            else:
                SQL = 'SELECT * FROM title where title="'+data[2]+'" and production_year="'+data[1]+'" and kind_id not in (6,7);'
            cursor.execute(SQL)
            results = cursor.fetchall()
        except:         #Here we handle the error
            print '<p>Something went wrong with the SQL!</p>'
            print SQL
            print "\nError:"
        else:
            # write if only one row is returned
            if(len(results)==1):
                writer.writerow(data+[results[0][0]])
                count_s+=1
            else:
                writer.writerow(data)
                if(len(results)>1):
                    count_m+=1
                else:
                    count_e+=1

#print the results
print "The number of movie titles matched :"+str(count_s)
print "The number of movie title missing :"+str(count_e)
print "The number of movie title with multiple entries :"+str(count_m)

