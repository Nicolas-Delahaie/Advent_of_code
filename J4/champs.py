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

def incluDans (e1, e2):
    '''regarde si lensemble 1 est contenu dans lensemble 2'''
    if e1[0] >= e2[0] and e1[1] <= e2[1]:
        return True
    else:
        return False

#Verification du nombre d erreurs pour chaque couple
nbPb = 0
for i in range(len(paires)):
    champ1 = paires[i][0]
    champ2 = paires[i][1]
    if incluDans(champ1, champ2) or incluDans(champ2, champ1):
        nbPb +=1
print(nbPb)
