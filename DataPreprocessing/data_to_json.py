"""
Pull data from netflix dataset and use the data saved from imdb dataset and write to json files to be imported to mongodb
"""
import csv,os
import json


__author__="Satvik Shetty"

#Use the file that has the mmatch between netflixID and IMDb ID
data=[line for line in csv.reader(open("imdb_link_p2.csv","r"))]
#Read the file that has imdb data saved
read_file=open("imdb_data.txt",'r')
data2=read_file.readlines()
read_file.close()

#Keep a count to split the json files we ae writing to divide input data to chunks
index=0
m=0
n=0
num=0
os.chdir(os.path.join(os.getcwd(),"training_setcsv"))
count=0
while(num<=9):
    #json filename where we save the data
    fln="jsonnetflix"+str(num)+".json"
    with open(fln,"w",newline='') as f:
        #Save the data in json array format using dictionaries
        f.write('[')
        for item in data[m:]:
            n=n+1
            if len(item)==4 and item[3]!='':
                print(item[0])
                #Read from user rating files of netflix Dataset
                filename="mv_"+"0"*(7-len(item[0]))
                filename+=str(item[0])+".csv"

                #save values in dictionary format to be later saved in json files
                dict1={}
                dict1["NetflixID"]=int(item[0])
                dict1["Title"]=item[2]
                dict1["Production_Year"]=item[1]
                iddata=[row for row in csv.reader(open(filename,"r"))]
                ld2=[]
                for i in iddata:
                    dict2={}
                    dict2["CustID"]=int(i[1])
                    dict2["UserRating"]=float(i[2])
                    if(len(i[3].split('-'))==3):
                        dict2["ReviewDay"]=i[3].split('-')[2]
                        dict2["ReviewMonth"]=i[3].split('-')[1]
                        dict2["ReviewYear"]=i[3].split('-')[0]
                    elif(len(i[3].split('/'))==3):
                        dict2["ReviewDay"]=i[3].split('/')[2]
                        dict2["ReviewMonth"]=i[3].split('/')[1]
                        dict2["ReviewYear"]=i[3].split('/')[0]
                    else:
                        print("Error")
                        print("Netflix id:"+str(item[0]))
                        print(i)
                        print("Custid :"+str(i[1]))
                        
                    ld2.append(dict2)
                dict1["Customer_Reveiws"]=ld2
                imdb_data=data2[index].split('|')
                dict1["MovieType"]=imdb_data[1]
                dict1["Director"]=imdb_data[2]
                genres=[]
                for j in imdb_data[3].strip().split(';'):
                    genres.append(j)
                dict1["Genre"]=genres
                json.dump(dict1, f)
                index=index+1
                if(index%1000==0):
                    print("break")
                    m=n
                    num=num+1
                    break
                if(int(item[0])==17770):
                    print("break")
                f.write(',\n')
        f.write(']')
print("Json file created :)")
