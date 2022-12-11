fic = open("msg.txt", "r")
datas = fic.read()
fic.close()

paires = datas.split("\n")

#Structuration
for i in range(len(paires)):
    paires[i] = paires[i].split(",")
for i in range(len(paires)):
    for n in range(2):
        paires[i][n] = paires[i][n].split("-")
for i in range(len(paires)):
    for n in range(2):
        for k in range(2):
            paires[i][n][k] = int(paires[i][n][k])

def ontElmtsEnCommun(l1, l2):
    '''Indique si les 2 listes ont des elements en commun'''
    for elmt1 in l1:
        for elmt2 in l2:
            if elmt1 == elmt2:
                return True
    return False

def chevauche (e1, e2):
    '''regarde si lensemble 1 est contenu dans lensemble 2'''
    #Transformation de l ensemble en suite de nombres
    e1 = list(range(e1[0],e1[1]+1))
    e2 = list(range(e2[0],e2[1]+1))
    if ontElmtsEnCommun(e1, e2):
        return True
    else:
        return False



#Verification du nombre d erreurs pour chaque couple
nbPb = 0
for i in range(len(paires)):
    champ1 = paires[i][0]
    champ2 = paires[i][1]
    if chevauche(champ1, champ2) or chevauche(champ2, champ1):
        nbPb +=1
print(nbPb)
