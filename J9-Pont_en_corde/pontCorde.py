fic = open("msg.txt", "r")
datas = fic.read()
fic.close()


#Structuration des instruction
instructionsGroupees = datas.split("\n")
for i in range(len(instructionsGroupees)):
    ligneInstruction = instructionsGroupees[i]
    
    #Separation instruction et nb
    instructionsGroupees[i] = ligneInstruction.split(" ")
    
    #U,R,D,L --> (+x, +y)
    if ligneInstruction[0] == "U":
        instructionsGroupees[i][0] = (0, -1)
    elif ligneInstruction[0] == "L":
        instructionsGroupees[i][0] = (-1, 0)
    elif ligneInstruction[0] == "D":
        instructionsGroupees[i][0] = (0, 1)
    elif ligneInstruction[0] == "R":
        instructionsGroupees[i][0] = (1, 0)
        
    instructionsGroupees[i][1] = int(instructionsGroupees[i][1])


def ajoutCoord(coords, ajout):
    """Ajout a un coordonnee (x,y) une coordonnee (+x,+y)"""
    newCoord = []
    for i in range(2):
        newCoord.append(coords[i]+ajout[i])
    return newCoord

def noeudsEcartes(coord1, coord2):
    deltaX = abs(coord1[0]-coord2[0])
    deltaY = abs(coord1[1]-coord2[1])
    if deltaX <= 1 and deltaY <= 1:
        #Noeuds colles
        return False
    else:
        #Noeuds ecartes de plus d une case
        return True
    
def dimensionsGrille(instructionsGroupees):
    """Retourne les coordonnees min et max et x et y de la forme (xmin,xmax),(ymin,ymax)"""
    x = 0
    xmin = float("inf")
    xmax = 0
    y = 0
    ymin = float("inf")
    ymax = 0
    for instructionGroupee in instructionsGroupees:
        for loop in range(instructionGroupee[1]):
            x += instructionGroupee[0][0]
            y += instructionGroupee[0][1]
        
        if y < ymin:
            ymin = y
        elif y > ymax:
            ymax = y
        if x < xmin:
            xmin = x
        elif x > xmax:
            xmax = x
        
    return ((xmin,xmax), (ymin,ymax))

def executeInstructions(instructionsGroupees, dimensions):
    """Execute les instructions de deplacement de la corde
       Renvoie les coordonnees de la queue et de la tete de la corde apres mouvements"""
    long = dimensions[1][1] - dimensions[1][0] + 1
    larg = dimensions[0][1] - dimensions[0][0] + 1
    casesVisitees = [[False for loop in range(larg)]for loop in range(long)]
    #Coordonnees du debut
    
    
    coordQ = [-dimensions[0][0], -dimensions[1][0]]
    coordT = coordQ
    casesVisitees[coordQ[1]][coordQ[0]]= True
    print("Coords dde debut :",coordQ[0],",",coordQ[1])
    
    for instructionGroupee in instructionsGroupees:
        for loop in range(instructionGroupee[1]):            
            ancienneT = coordT
            coordT = ajoutCoord(coordT, instructionGroupee[0])
            if noeudsEcartes(coordQ, coordT):
                #Si la queue est separee de la tete
                if coordQ[0]==coordT[0]:
                    #Sur la meme colonne
                    if coordQ[1] < coordT[1]:
                        #Tete en dessous de queue
                        coordQ[1] += 1
                    else:
                        #Tete au dessus de queue
                        coordQ[1] -= 1
                        
                if coordQ[1]==coordT[1]:
                    #Sur la meme ligne
                    if coordQ[0] < coordT[0]:
                        #Tete a droite de queue
                        coordQ[0] += 1
                    else:
                        #Tete a gauche de queue
                        coordQ[0] -= 1
                    
                else:
                    #Sur une rangee differente
                    coordQ = ancienneT
                    
                #Sauvegarde de la case visitee par la queue
                xQ = coordQ[0]
                yQ = coordQ[1]
                casesVisitees[yQ][xQ] = True
                    
    return casesVisitees

def afficheGrille(grille):
    for ligne in grille:
        for case in ligne:
            if case:
                print("1 ", end="")
            else:
                print("0 ",end="")
        print("")
            
def nbCasesVisitees(casesVisitees):
    """Renvoie le nombre de cases visitees"""
    compteur = 0
    for ligne in casesVisitees:
        for case in ligne:
            if case:
                compteur += 1
    return compteur



dimensions = dimensionsGrille(instructionsGroupees)
print("Dimensions :",dimensions)
casesVisitees = executeInstructions(instructionsGroupees,dimensions)
print("Nombre de cases visitees:",nbCasesVisitees(casesVisitees))


