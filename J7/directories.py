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
        
    def sommeDossier (self):
        """Retourne la somme de tous les fichiers descendants de self"""
        somme = 0
        for enfant in self._contenu:
            if isinstance(enfant, Dossier):
                #Dossier
                somme += enfant.sommeDossier()
            else:
                #Fichier (condition d arret)
                somme += enfant
        return somme
    
    def ajoutDossiersInferieursA(self, somme, tailleMax = 100000):
        """Retourne la somme de tous les dossiers descendants de self ayant une taille inferieure a tailleMax"""
        sommeTotale = self.sommeDossier()
        if sommeTotale <= tailleMax:
            somme.append(sommeTotale)
        for sousDossier in self._contenu:
            if isinstance(sousDossier, Dossier):
                sousDossier.ajoutDossiersInferieursA(somme)
    
    
    
def lignesConsolesINTODossier(lignesConsole):
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
                
                print(ligne)
                print(source)
                #print(source.getSousDossier(emplacementCourant))
                source.getSousDossier(emplacementCourant).ajouter(tailleFic)
    return source
            
source = lignesConsolesINTODossier(lignesConsole)
print(source)
print(source.sommeDossier())
dossiersOk = []
source.ajoutDossiersInferieursA(dossiersOk)
print(sum(dossiersOk))
