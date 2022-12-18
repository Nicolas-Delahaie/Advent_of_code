fic = open("msg.txt", "r")
datas = fic.read()
fic.close()

lignesConsole = datas.split("\n")
lignesConsole.remove("$ cd /")

class Dossier:
    """Definition d un dossier"""
    def __init__(self, nom:str, contenu = None):
        self._nom = nom
        self._contenu = contenu if contenu else []
    def __repr__(self):
        return self.__str__()
    def __str__ (self, profondeur = 0):
        '''Retourne le dossier de maniere graphique'''
        msg = "- "+self._nom+"\n"
        profondeur += 1
        for enfant in self._contenu:
            for loop in range(profondeur):
                msg += "| "
            if isinstance(enfant, Dossier):
                #Dossier
                msg += enfant.__str__(profondeur)
            else:
                #Condition d arret : ne pas etre un dossier
                msg += "- "+str(enfant)+"\n"
        return msg
        
    
    def getSousDossier(self, arborescence=[]):
        if (arborescence == []):
            #Le dossier courant est celui recherche par larborescence
            return self
        else:
            for i in range(len(self._contenu)):
                #Pour chaque enfant
                if not isinstance(self._contenu[i], int):                    
                    #L element est un dossier
                    if self._contenu[i]._nom ==  arborescence[0]:
                        #Le dossier correspondant a celui recherche
                        newArbo = arborescence.copy()
                        newArbo.pop(0)
                        return self._contenu[i].getSousDossier(newArbo)
                        break
        return "Fichier inexistant"
        
    def ajouter (self, elmt):
        self._contenu.append(elmt)
        
    def tailleDossier (self):
        """Retourne la somme de tous les fichiers descendants de self"""
        somme = 0
        for enfant in self._contenu:
            if isinstance(enfant, Dossier):
                #Dossier
                somme += enfant.tailleDossier()
            else:
                #Fichier (condition d arret)
                somme += enfant
        return somme
    
    def ajoutDossiersInferieursA(self, somme, tailleMax = 100000):
        """Retourne la somme de tous les dossiers descendants de self ayant une taille inferieure a tailleMax"""
        sommeTotale = self.tailleDossier()
        if sommeTotale <= tailleMax:
            somme.append(sommeTotale)
        for sousDossier in self._contenu:
            if isinstance(sousDossier, Dossier):
                sousDossier.ajoutDossiersInferieursA(somme)
    
    
    def plusPetiteTailleSuperieureA(self, tailleMin, tailleADepasser):
        """Retourne la taille du fichier parmi de tous les dossiers descendants de self ayant la taille la plus petite, superieure a tailleADepasser"""
        tailleDossier = self.tailleDossier()
        #la plus petite taille devient celle du dossier si elle est inferiere a celle d avant
        if tailleADepasser < tailleDossier and tailleDossier < tailleMin[0]:
            tailleMin[0] = tailleDossier
            
            
        for sousDossier in self._contenu:
            if isinstance(sousDossier, Dossier):
                sousDossier.plusPetiteTailleSuperieureA(tailleMin, tailleADepasser)
    
def dossierFROMLignes(lignesConsole):
    source = Dossier("source")
    emplacementCourant = []
    for ligne in lignesConsole:
        if ((ligne[2:4] == "cd")):
            #Change directory
            if (ligne[-2:] == ".."):
                #cd Retour
                emplacementCourant.pop()
            else:
                #cd Repertoire
                emplacementCourant.append(ligne[5:])
            
        elif (ligne[:3] == "dir"):
            #Creer repertoire
            source.getSousDossier(emplacementCourant).ajouter(Dossier(ligne[4:]))
            
        else:
            if (ligne[:4] != "$ ls"):
                #Creer fichier
                tailleFic = int(ligne.split(" ")[0])
                source.getSousDossier(emplacementCourant).ajouter(tailleFic)
    return source
            
source = dossierFROMLignes(lignesConsole)
print(source)

tailleSource = source.tailleDossier()
print("TailleSource :",tailleSource)

dossiersOk = []
source.ajoutDossiersInferieursA(dossiersOk)
print("Somme dossiers inferieurs a 100000 :",sum(dossiersOk))

espaceTotal = 70000000
espaceNecessaire = 30000000
espaceLibre = espaceTotal - tailleSource
espaceALiberer = espaceNecessaire - espaceLibre
plusPetiteTaille = [float("inf")]
source.plusPetiteTailleSuperieureA(plusPetiteTaille, espaceALiberer)
print("Taille du dossier a liberer :", plusPetiteTaille[0])



