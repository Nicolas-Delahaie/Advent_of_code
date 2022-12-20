from graphics import *
import time

fic = open(__file__ + "/../msgTest.txt", "r")
datas = fic.read()
fic.close()
class Noeud:
    def __init__(self,x,y):
        self.x = x
        self.y = y
    def __str__(self):
        return "("+str(self.x)+":"+str(self.y)+")"
    def __repr__(self):
        return self.__str__()

    def copy(self):
        return Noeud(self.x, self.y)
    
    def deplacer(self, direction):
        if not isinstance(direction, Direction):
            print("Vous devez utiliser une direction")
        else:
            self.x += direction.x
            self.y += direction.y
    def estColleA(self, Noeud):
        """Indique si la Noeud est a moins d une case"""
        deltaX = abs(self.x - Noeud.x)
        deltaY = abs(self.y - Noeud.y)
        if deltaX <= 1 and deltaY <= 1:
            #Noeuds colles
            return True
        else:
            #Noeuds ecartes de plus d une case
            return False    
    def distance(self,Noeud):
        """Renvoie la distance en nombre de cases a parcourir pour rejoindre l'autre point"""
        deltaX = abs(self.x - Noeud.x)
        deltaY = abs(self.y - Noeud.y)
        return (deltaX, deltaY)
    def suivre(self, noeud, ancienneTete):
        """Modifie le noeud de maniere a le positionner colle au noeud en parametre"""
        noeudAvantModif = self.copy()
        if not self.estColleA(noeud):
            #Il necessite d etre raproche du noeud
            self.x = ancienneTete.x
            self.y = ancienneTete.y
        return noeudAvantModif         
class Corde:
    def __init__(self,nbNoeuds, NoeudDepart):
        self.taille = nbNoeuds
        self.noeuds = []
        for loop in range(nbNoeuds):
            self.noeuds.append(NoeudDepart.copy())
    def __str__(self):
        msg = self.noeuds[0].__str__()
        for i in range(1,len(self.noeuds)):
            msg += " <- "+self.noeuds[i].__str__()
        return msg
    def __repr__(self):
        return self.__str__()
    
    def deplacerTete(self, direction):
        #Deplacement de la tete
        ancienNoeud = self.noeuds[0].copy()
        self.noeuds[0].deplacer(direction)

        noeudSuivant = 1
        while noeudSuivant < self.taille :
            if not self.noeuds[noeudSuivant].estColleA(self.noeuds[noeudSuivant-1]):
                #Si le noeud suivant suivant n est pas colle, le deplacer
                ancienNoeud = self.noeuds[noeudSuivant].suivre(self.noeuds[noeudSuivant-1], ancienNoeud)
                noeudSuivant += 1
            else:
                break
        
    def executeInstructions(self, instructionsGroupees, casesVisitees):
        """Execute les instructions de deplacement de la corde"""

        casesVisitees.grille[self.noeuds[-1].y][self.noeuds[-1].x] = True
        for instructionGroupee in instructionsGroupees:
            for loop in range(instructionGroupee[1]):
                print(self.noeuds, instructionGroupee[0])
                self.deplacerTete(instructionGroupee[0])
                casesVisitees.grille[self.noeuds[-1].y][self.noeuds[-1].x] = True
               
        return casesVisitees
class Direction:
    def __init__(self,x,y=None):
        """Constructeur avec x et y pour le vecteur ou bien U,R,D ou L"""
        if y == None:
            #x represente la direction : U,R,D ou L
            
            if x == "U":
                self.x = 0
                self.y = -1
            elif x == "R":
                self.x = 1
                self.y = 0
            elif x == "D":
                self.x = 0
                self.y = 1
            elif x == "L":
                self.x = -1
                self.y = 0
            else:
                print ("Mauvaise direction de vecteur")
                
        else:
            #x et y representent un vecteur
            if x>1 or y>1 or x==y:
                print("Vecteur incorect : il doit deplacer d une seule case")
            else:
                self.x = x
                self.y = y
    def __str__(self):
        if self.x == 1:
            sens = "Droite"
        elif self.x == -1:
            sens = "Gauche"
        elif self.y == 1:
            sens = "Bas"
        elif self.y == -1:
            sens = "Haut"
        return sens
    def __repr__(self):
        return self.__str__()
class Grille:
    def __init__(self, larg = 0, long = 0):
        self.larg = larg
        self.long = long
        if larg != 0 and long != 0:
            self.initGrille()
        else:
            self.grille = None
    def __repr__(self):
        return self.__str__()
    def __str__(self):
        msg = ""
        for ligne in self.grille:
            for case in ligne:
                if case:
                    msg += " 1 "
                else:
                    msg += " 0 "
            msg += "\n"
        return msg

    def initGrille(self):
        self.grille = [[False for loop in range(self.larg)] for loop in range(self.long)]
    def calculerDimensions(self, instructionsGroupees):
        """Retourne les Noeudonnees du premier point dans la grille avec ses dimensions de la forme (larg, long, NoeudDebut)"""
        x = 0
        xmin = float("inf")
        xmax = 0
        y = 0
        ymin = float("inf")
        ymax = 0
        for instructionGroupee in instructionsGroupees:
            for loop in range(instructionGroupee[1]):
                x += instructionGroupee[0].x
                y += instructionGroupee[0].y
            
            if y < ymin:
                ymin = y
            elif y > ymax:
                ymax = y
            if x < xmin:
                xmin = x
            elif x > xmax:
                xmax = x

        larg = xmax - xmin + 1
        long = ymax - ymin + 1
        coordDepart = Noeud(-xmin, -ymin)
        
        self.larg = larg
        self.long = long
        self.initGrille()

        return coordDepart
    def sommeCasesVisitees(self):
        """Renvoie le nombre de cases visitees"""
        compteur = 0
        for ligne in self.grille:
            for case in ligne:
                if case:
                    compteur += 1
        return compteur   
class Fenetre:
    def __init__(self, nom, larg, long, corde, instructionsGroupees):
        self.nom = nom
        self.larg = larg
        self.long = long
        self.corde = corde
        self.lignes =[]
        self.win = GraphWin(nom,larg,long)
        
        self.initPoints()
        self.actualiserCorde()
        self.afficherPoints()
        
        etape = 0 #Numero de l instruction en cours
        limite = len(instructionsGroupees)
        while(self.win.checkKey() == ""):
            #Annimation corde
            time.sleep(0.05)
            self.attendreClic()
            if etape < limite:
                #Corde pas finie d etre affichee
                for loop in range(instructionsGroupees[etape][1]):
                    self.corde.deplacerTete(instructionsGroupees[etape][0])
                    self.actualiserCorde()

        self.win.close()
    
    def initPoints(self):
        for loop in range(self.corde.taille) :
            self.lignes.append(Line(Point(0,0)),Line(Point(0,0)))
    def afficherPoints(self):
        for i in range(len(self.points)):
            self.points[i].draw(self.win)
    def actualiserCorde(self):
        for i in range(self.corde.taille):
            noeud = self.corde.noeuds[i]
            self.points[i].x = noeud.x
            self.points[i].y = noeud.y
            update()
    def attendreClic(self):
        NoeudClic = self.win.checkMouse()
        if  NoeudClic!= None:
            #Clic de la souris
            distance = self.corde.noeuds[0].distance(Noeud(NoeudClic.x, NoeudClic.y))
            deltaX = distance[0]
            deltaY = distance[1]


#Structuration des instruction
instructionsGroupees = datas.split("\n")
for i in range(len(instructionsGroupees)):
    # -- Transformation des U,L,D,R en vecteurs --
    instructionsGroupees[i] = instructionsGroupees[i].split(" ")
    instructionsGroupees[i][0] = Direction(instructionsGroupees[i][0])
    instructionsGroupees[i][1] = int(instructionsGroupees[i][1])

# -- Creation casesVisitees --
casesVisitees = Grille()
coordDepart = casesVisitees.calculerDimensions(instructionsGroupees)
print("Coord de depart :",coordDepart,"\n")

# -- Creation de la corde --
corde = Corde(10, coordDepart)
corde.executeInstructions(instructionsGroupees, casesVisitees)
print("Cases visitees :")
print(casesVisitees)
print("Nombre de cases visitees:",casesVisitees.sommeCasesVisitees(), "\n")

# -- Creation affichage --
# affichage = Fenetre("Cordes", larg, long, corde, instructionsGroupees)


# corde = Corde(2, Noeud(1,2))
# corde.deplacerTete(Direction("R"))
# print(corde)
# corde.deplacerTete(Direction("U"))
# print(corde)
# corde.deplacerTete(Direction("U"))
# print(corde)
# corde.deplacerTete(Direction("L"))
# print(corde)
# corde.deplacerTete(Direction("L"))
# print(corde)
# corde.deplacerTete(Direction("D"))
# print(corde)
# corde.deplacerTete(Direction("D"))
# print(corde)
# corde.deplacerTete(Direction("D"))
# print(corde)

