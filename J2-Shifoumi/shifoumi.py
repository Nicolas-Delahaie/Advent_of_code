fic = open("msg.txt", "r")
datas = fic.read()
fic.close()

tours = datas.split("\n")

pointsFigures = {'A':1,'B':2,'C':3,'X':1,'Y':2,'Z':3}

#Transformation str en list
for i in range(len(tours)):
    new=[]
    new.append(tours[i][0])
    new.append(tours[i][2])
    tours[i] = new


def quiGagne (j1, j2):
    gagne =[[None,1,0],
            [0,None,1],
            [1,0,None]]
    indices = {'A':0,'B':1,'C':2,
               'X':0,'Y':1,'Z':2}
    return gagne[indices[j1]][indices[j2]]


def compteScores():
    scores = [0,0]
    for tour in tours:
        gagnant = quiGagne(tour[0], tour[1])
        #Ajout des points au gagnant
        if gagnant == None:
            scores[0] += 3
            scores[1] += 3
        else:
            scores[gagnant] +=6

        #Ajout des points grace a la figure
        scores[0] += pointsFigures[tour[0]]
        scores[1] += pointsFigures[tour[1]]
    return scores

print(compteScores[1])