fic = open("msg.txt", "r")
datas = fic.read()
fic.close()

champsArbres = datas.split("\n")

#Mise sous forme de tableau
for i in range(len(champsArbres)):
    new = []
    for arbre in champsArbres[i]:
        new.append(int(arbre))
    champsArbres[i] = new
    
    
def affichageChamps(champs):
    """Affiche de maniere graphique le champs d arbres"""
    for n in range(len(champsArbres[0])):
        #Pour chaque colonne
        for i in range(len(champsArbres)):
            #Pour chaque ligne
            print(champsArbres[n][i], end=" ")
        print("")

def scoreArbre(x,y):
    """Retourne le score avec les coordonnees x et y"""
    long = len(champsArbres)
    larg = len(champsArbres[0])
    scoresDirections=[0,0,0,0]
    
    # -- Pour chaque direction --
    #Gauche
    copieX = x - 1
    while copieX >= 0:
        scoresDirections[3] += 1
        if champsArbres[y][copieX] >= champsArbres[y][x]:
            break
        copieX -= 1
    #Droite
    copieX = x + 1
    while copieX < larg:
        scoresDirections[1] += 1
        if champsArbres[y][copieX] >= champsArbres[y][x]:
            break
        copieX += 1
    #Haut
    copieY = y - 1
    while copieY >= 0:
        scoresDirections[0] += 1
        if champsArbres[copieY][x] >= champsArbres[y][x]:
            break
        copieY -= 1
    #Bas
    copieY = y + 1
    while copieY < long:
        scoresDirections[2] += 1
        if champsArbres[copieY][x] >= champsArbres[y][x]:
            break
        copieY += 1         

    scoreArbre = scoresDirections[0]*scoresDirections[1]*scoresDirections[2]*scoresDirections[3]
    return scoreArbre
        
    
def meilleurArbre():
    """Retourne les coordonnees du meilleur arbre parmis tous ceux presents dans le champs"""
    meilleurArbre = 0
    
    for x in range(len(champsArbres[0])):
        for y in range(len(champsArbres)):
            score = scoreArbre(x,y)
            if score > meilleurArbre:
                meilleurArbre = score
    
    return meilleurArbre
    

affichageChamps(champsArbres)
print(meilleurArbre())




