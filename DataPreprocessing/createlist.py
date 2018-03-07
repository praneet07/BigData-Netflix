#@Author Rohan Ingale
#to fetch the data from mongodb in the form of list

from pymongo import MongoClient
#get an instance of mongo client
client = MongoClient()
#connect to a database in mongodb
db = client['BigDataProjectTest']
#get the collection in which data is loaded
collection = db['sampleData']
def createlistfunc():
	#fetch records in cursor
	cursor1 = collection.find()

	list3 = list()
	i = 0

	#iterate over all the records and fetch the required details
	for record in cursor1:
		list1 = list()
		list1.append(record['NetflixID'])
		list1.append(record['Production_Year'])
		list1.append(record['Title'])
		list1.append(record['Genre'])
		list1.append(record['Director'])
		list1.append(record['MovieType'])
		#iterate over the customer review list
		for reviews in record['Customer_Reveiws']:
			list2 = list()
			list2.append(reviews['CustID'])
			list2.append(reviews['ReviewYear'])
			list2.append(reviews['UserRating'])
			list1.append(list2)
	return list1