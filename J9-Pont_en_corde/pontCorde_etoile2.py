from graphics import *
import time

fic = open(__file__ + "/../msg.txt", "r")
datas = fic.read()
fic.close()


class Noeud:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return "(" + str(self.x) + ":" + str(self.y) + ")"

    def __repr__(self):
        return self.__str__()

    def copy(self):
        return Noeud(self.x, self.y)

    def deplacer(self, direction):
        """Deplace le noeud dans la direction souhaitee.
        Renvoie le noeud avant deplacement"""
        noeudAvantModif = self.copy()
        self.x += direction.x
        self.y += direction.y
        return noeudAvantModif

    def estColleA(self, Noeud):
        """Indique si la Noeud est a moins d une case"""
        deltaX = abs(self.x - Noeud.x)
        deltaY = abs(self.y - Noeud.y)
        if deltaX <= 1 and deltaY <= 1:
            # Noeuds colles
            return True
        else:
            # Noeuds ecartes de plus d une case
            return False

    def distance(self, Noeud):
        """Renvoie la distance en nombre de cases a parcourir pour rejoindre l'autre point"""
        deltaX = abs(self.x - Noeud.x)
        deltaY = abs(self.y - Noeud.y)
        return (deltaX, deltaY)

    def suivre(self, noeud):
        """Pre-condition : les 2 noeuds sont separes
        Modifie le noeud de maniere a le positionner colle au noeud en parametre"""
        if self.estColleA(noeud):
            raise Exception("Les deux noeuds ne doivent pas etres colles")

        if self.x > noeud.x:
            # Noeud a droite de celui a suivre
            self.x -= 1
        elif self.x < noeud.x:
            # Noeud a gauche de celui a suivre
            self.x += 1

        if self.y > noeud.y:
            # Noeud en bas de celui a suivre
            self.y -= 1
        elif self.y < noeud.y:
            # Noeud en haut de celui a suivre
            self.y += 1

        if not self.estColleA(noeud):
            raise Exception("PROGRAMME NON FONCTIONNEL")


class Corde:
    def __init__(self, nbNoeuds, NoeudDepart):
        self.taille = nbNoeuds
        self.noeuds = []
        for loop in range(nbNoeuds):
            self.noeuds.append(NoeudDepart.copy())

    def __str__(self):
        msg = self.noeuds[0].__str__()
        for i in range(1, len(self.noeuds)):
            msg += " <- " + self.noeuds[i].__str__()
        return msg

    def __repr__(self):
        return self.__str__()

    def deplacerTete(self, direction):
        """Deplace la tete dans la direction souhaitee, en adaptant tous les noeuds suivants"""
        # Deplacement de la tete
        self.noeuds[0].deplacer(direction)

        nextNodeIndex = 1
        while nextNodeIndex < self.taille:
            nextNode = self.noeuds[nextNodeIndex]
            if nextNode.estColleA(self.noeuds[nextNodeIndex - 1]):
                break
            else:
                # Si le noeud suivant suivant n est pas colle, le deplacer
                nextNode.suivre(self.noeuds[nextNodeIndex - 1])
                nextNodeIndex += 1

    def executeInstructions(self, instructionsGroupees, casesVisitees):
        """Execute les instructions de deplacement de la corde"""

        casesVisitees.setVisited(self.noeuds[-1])
        for instructionGroupee in instructionsGroupees:
            for loop in range(instructionGroupee[1]):
                self.deplacerTete(instructionGroupee[0])
                casesVisitees.grille[self.noeuds[-1].y][self.noeuds[-1].x] = True

        return casesVisitees


class Direction:
    def __init__(self, x, y=None):
        """Constructeur avec x et y pour le vecteur ou bien U,R,D ou L"""
        if y == None:
            # x represente la direction : U,R,D ou L

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
                print("Mauvaise direction de vecteur")

        else:
            # x et y representent un vecteur
            if x > 1 or y > 1 or x == y:
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
    def __init__(self, larg=0, long=0):
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
        self.grille = [
            [False for loop in range(self.larg)] for loop in range(self.long)
        ]

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

    def setVisited(self, noeud):
        self.grille[noeud.y][noeud.x] = True

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
        self.lignes = []
        self.win = GraphWin(nom, larg, long)

        self.initPoints()
        self.actualiserCorde()
        self.afficherPoints()

        etape = 0  # Numero de l instruction en cours
        limite = len(instructionsGroupees)
        while self.win.checkKey() == "":
            # Annimation corde
            time.sleep(0.05)
            self.attendreClic()
            if etape < limite:
                # Corde pas finie d etre affichee
                for loop in range(instructionsGroupees[etape][1]):
                    # self.corde.deplacerTete(instructionsGroupees[etape][0])
                    self.actualiserCorde()

                for instructionGroupee in instructionsGroupees:
                    for loop in range(instructionGroupee[1]):
                        self.deplacerTete(instructionGroupee[0])

        self.win.close()

    def initPoints(self):
        for loop in range(self.corde.taille):
            self.lignes.append(Line(Point(0, 0), Point(0, 0)))

    def afficherPoints(self):
        for i in range(self.corde.taille):
            self.lignes[i].draw(self.win)

    def actualiserCorde(self):
        for i in range(1, self.corde.taille):
            noeudAvant = self.corde.noeuds[i - 1]
            noeud = self.corde.noeuds[i]

            self.lignes[i - 1].x = noeudAvant.x
            self.lignes[i - 1].y = noeudAvant.y

            self.lignes[i].x = noeud.x
            self.lignes[i].y = noeud.y
            update()

    def attendreClic(self):
        NoeudClic = self.win.checkMouse()
        if NoeudClic != None:
            # Clic de la souris
            distance = self.corde.noeuds[0].distance(Noeud(NoeudClic.x, NoeudClic.y))
            deltaX = distance[0]
            deltaY = distance[1]


# Structuration des instruction
instructionsGroupees = datas.split("\n")
for i in range(len(instructionsGroupees)):
    # -- Transformation des U,L,D,R en vecteurs --
    instructionsGroupees[i] = instructionsGroupees[i].split(" ")
    instructionsGroupees[i][0] = Direction(instructionsGroupees[i][0])
    instructionsGroupees[i][1] = int(instructionsGroupees[i][1])

# -- Creation casesVisitees --
casesVisitees = Grille()
coordDepart = casesVisitees.calculerDimensions(instructionsGroupees)
print("Coord de depart :", coordDepart)

# -- Creation de la corde --
corde = Corde(10, coordDepart)
corde.executeInstructions(instructionsGroupees, casesVisitees)
print("Nombre de cases visitees:", casesVisitees.sommeCasesVisitees())

# -- Creation affichage --
# affichage = Fenetre("Corde", casesVisitees.larg, casesVisitees.long, corde, instructionsGroupees)
