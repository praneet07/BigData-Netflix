"""
Pull all necessary data from IMDb tables using the link between netflixID and IMDb ID
"""

#! /usr/bin/env python
import MySQLdb,csv

__author__="Satvik Shetty"

#establish DB connection
string = "************"     #change this to yours
password = "**************"    #change this to yours
db_con = MySQLdb.connect(host="db.soic.indiana.edu", port = 3306, user=string, passwd=password, db=string)
cursor = db_con.cursor()

SQL1=""
SQL2=""
SQL3=""

#Refering the csv file that has the link between netflixID and IMDb ID
NetflixRow=[line for line in csv.reader(open("imdb_link_p2.csv","r"))]

#Save all relevant imdb data in a file
with open("test.txt","w") as f:
    for data in NetflixRow:
        info=""
        if len(data)==4:
            info+=data[3]+"|"
            try:
                #SQL queries to retrieve kind type,genre and directors name
                SQL1="SELECT kind FROM kind_type,title WHERE kind_id=kind_type.id and title.id='"+data[3]+"';"
                cursor.execute(SQL1)
                results1 = cursor.fetchall()
                SQL2="SELECT name FROM cast_info,name WHERE person_id=name.id and movie_id='"+data[3]+"' and role_id='8';"
                cursor.execute(SQL2)
                results2 = cursor.fetchall()
                SQL3="SELECT info FROM movie_info WHERE info_type_id='3' and movie_id='"+data[3]+"';"
                cursor.execute(SQL3)
                results3 = cursor.fetchall()
            except:         #Here we handle the error
                print '<p>Something went wrong with the SQL!</p>'
                print SQL1
                print SQL2
                print SQL3
                print "\nError:"
            else:
                #concatenate the results and write to file
                info+=results1[0][0]+"|"
                for i in results2:
                    info+=i[0]+";"
                info=info.rstrip(";")+"|"
                for i in results3:
                    info+=i[0]+";"
                info=info.rstrip(";")
                f.write(info+"\n")
                
                    
