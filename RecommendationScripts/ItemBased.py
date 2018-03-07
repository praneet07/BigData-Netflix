"""
Includes the algorithm for item based collaborative filtering algorithm
"""

from math import sqrt
from RecommendationScripts import dataset as d

__author__="Satvik Shetty"

##Function to modify the data from the sample input
##Irrelevant for the main main project
"""
def swapData(userbased):
    itembased={}
    for user in userbased:
        for item in userbased[user]:
            itembased.setdefault(item,{})
            itembased[item][user]=userbased[user][item]
    return itembased
"""

#Calculates the similarity score between two movies
def pearsonsim(itembased,item1,item2):

    #initializing variables
    i1rating_sum = 0
    i2rating_sum = 0
    i1rating_powsum = 0
    i2rating_powsum = 0
    i1i2rating_product = 0
    count_sim=0
    denom=None
    numer = None
    for usr in itembased[item1]:
        if usr in itembased[item2]:

            #compute the values needed to calculate the pearsons corelation
            count_sim+=1
            i1rating_sum += itembased[item1][usr]
            i2rating_sum += itembased[item2][usr]
            i1rating_powsum += pow(itembased[item1][usr],2)
            i2rating_powsum += pow(itembased[item2][usr], 2)
            i1i2rating_product+=(itembased[item1][usr]*itembased[item2][usr])

    if count_sim == 0:
        #return 0 in case there is no similarity
        return 0
    else:
        #calculating pearsons corelation
        denom = sqrt(((i1rating_powsum-(pow(i1rating_sum,2)/count_sim))*(i2rating_powsum - (pow(i2rating_sum,2)/count_sim))))

        #return zero in case the denominator value is zero
        if denom == 0:
            return 0
        else:
            numer=i1i2rating_product-((i1rating_sum*i2rating_sum)/count_sim)
            return numer/denom


#Funtcion to calculate the similarity matrix
def similarity_matrix(itembased):

    #initialize dictionary to save the similarity matrix
    simmat={}
    for item in itembased:
        temp=[]
        for i in itembased:
            if i != item:

                #call the pearsonsim function to calculate similarity
                score=pearsonsim(itembased,item,i)
                if score!=0:
                    temp.append((score,i))
        simmat[item]=sorted(temp,reverse=True)
    return simmat


#Function that takes a customer id and returns a list of recommendations for that user
def recommendation(userpref,itembased,simmat,user):
    pref_data={}
    sim_score_total={}
    movie_score=[]

    #Loop over all the movies watched by the user
    for (movie,rating) in userpref.items():
        #Loop over all the movies similar to the current movie
        for(sim_score,sim_movie) in simmat[movie]:
            #Check if movie isnt already watched by user
            if sim_movie not in userpref.keys():
                pref_data.setdefault(sim_movie,0)
                sim_score_total.setdefault(sim_movie,0)
                pref_data[sim_movie]+=sim_score*rating
                sim_score_total[sim_movie]+=sim_score
    for (movie,total_rating) in pref_data.items():
        # calculate user predicted rating and save as (rating,movie) so it can be sorted
        movie_score.append((total_rating/sim_score_total[movie],movie))

    #return the list of recommendation in descending order
    return sorted(movie_score,reverse=True)



"""
#Main function for running algorithm on sample dataset

data=(swapData(d.dataex))
#print(data)


#print(pearsonsim(data,'Lady in the Water','Snakes on a Plane'))
simmat=similarity_matrix(data)
for i in simmat.items():
    print(i)
print(recommendation(d.dataex,data,simmat,'Toby'))

"""