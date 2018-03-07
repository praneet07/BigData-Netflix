"""
Content filtering algorithm
"""


__author__="Saurav Chakraborty"


mid = input("enter movie id:")
for i in range(len(data)):
    movie = data[i]
     genre = []
    dir =[]
    kind = []
    for movie in data:

        if int(mid) == movie[3]:
            genre.append(movie[1])
            dir.append(movie[0])
            kind.append(movie[2])
print (genre, dir, kind)
gen = []
d = []
k = []
for i in range(len(genre[0])):
    gen.append(genre[0][i])
sim_list = []
for movie in data:
    similarity_score = 0
    g=[]
    for i in range(len(movie[1])):
        g.append(movie[1][i])

    for i in range(len(movie[1])):
        for j in range (len(gen)):

            if g[i] == gen[j]:
                similarity_score += 2


    for i in range(len(dir)):
        if movie[0] == dir[i]:
            similarity_score += 1

    if movie[2] == kind[0]:
        similarity_score += 1

    sim_list.append([movie[4], similarity_score])

s = sorted(sim_list, key=itemgetter(1), reverse = True)
res = s[0:50]

df = pd.DataFrame(res)