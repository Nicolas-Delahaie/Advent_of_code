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
    
    
def arbresAvantBordure(x,y):
    """Retourne une liste de coordonnes des arbres entre l arbre en (x,y) chaque bordure"""
    lCoords = []
    long = len(champsArbres)
    larg = len(champsArbres[0])
    # -- Pour chaque bordure --
    #Gauche
    lCoords.append([])
    copieX = x - 1
    while (copieX >= 0):
        lCoords[-1].append(champsArbres[y][copieX])
        copieX -= 1
        
    #Droite
    copieX = x + 1
    lCoords.append([])
    while (copieX < larg):
        lCoords[-1].append(champsArbres[y][copieX])
        copieX += 1
        
    #Haut
    lCoords.append([])
    copieY = y - 1
    while (copieY >= 0):
        lCoords[-1].append(champsArbres[copieY][x])
        copieY -= 1
        
    #Bas
    lCoords.append([])
    copieY = y + 1
    while (copieY < long):
        lCoords[-1].append(champsArbres[copieY][x])
        copieY += 1
        
    return lCoords

def estVisible(x,y):
    """Indique si l arbre de coordonnees x y est visible depuis le bord"""
    rangees = arbresAvantBordure(x,y)
    for rangee in rangees:
        rangeeLibre = True
        for arbre in rangee:
            if arbre >= champsArbres[y][x]:
                #Arbre plus grand que lui
                rangeeLibre = False
        if rangeeLibre:
            return True
    return False
    
def nbArbresVisibles():
    """Indique le nombre d arbres du champs visibles depuis le bord"""
    compteur = 0
    for x in range(len(champsArbres[0])):
        for y in range(len(champsArbres)):
            if estVisible(x,y):
                compteur += 1        
    return compteur
    
print(nbArbresVisibles())

