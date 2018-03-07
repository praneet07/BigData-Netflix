#@author: Rohan Ingale
#code to split the netflix_imdb data present in file into 10 chunks, each of 1000 records and store them into separate files

#open the file in read mode 
reader = open("jsonetflix_imdb.json","r")
count = 0
fileNumber = 1
#open the new file in write mode to write a chunk
writer = open("output"+str(fileNumber)+".json","a")

#read line by line from input file
line  = reader.readline()
while line:
	count += 1
	writer.write(line)
	#print(line)
	line  = reader.readline()
	#to check if 1000 records are read
	if(count>1000):
		writer.close()
		fileNumber+=1
		#open a new file to write next 1000 records
		writer = open("D:/CD/Sp16/output"+str(fileNumber)+".txt","a")
		print(str(fileNumber) + "has "+str(count)+" lines.")
		count = 0

print(str(count))
reader.close()			
writer.close()