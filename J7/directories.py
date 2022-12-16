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
        
    def sommeFichiers (self, tailleMax = 100000):
        somme = 0
        for enfant in self._contenu:
            if isinstance(enfant, Dossier):
                #Dossier
                somme += enfant.sommeFichiers()
            else:
                #Condition d arret : ne pas etre un dossier
                if enfant < tailleMax:
                    somme += enfant
        return somme
    
    def __repr__(self):
        return self.__str__()
    
    def __str__ (self, profondeur = 0):
        '''Retourne le dossier de la maniere suivante :
            doss(doss1(), doss2(11), 11, doss3(doss4(11,11), doss5()))'''
        
        
        msg = "- "+self._nom+"\n"
        
        profondeur += 1
        for enfant in self._contenu:
            for loop in range(profondeur):
                msg += "  "
            if isinstance(enfant, Dossier):
                #Dossier
                msg += enfant.__str__(profondeur)
            else:
                #Condition d arret : ne pas etre un dossier
                msg += "- "+str(enfant)+"\n"


        return msg

"""

- source
  - a
    - e
      827749
  - b
  - c

"""
source = Dossier("source", [
            Dossier("a", [
                Dossier("e",[
                    584]),
                29116,
                2557,
                62596]),
            14848514,
            8504156,
            Dossier("d", [
                4060174,
                8033020,
                5626152,
                7214296])])


#source.getSousDossier(["d"]).ajouter(Dossier("x", []))
#source.getSousDossier(["d", "x"]).ajouter(999)
#print(source.getSousDossier(["d","x"])._contenu)
#print("somme =",source.sommeFichiers())

#print(source.sommeFichiers())
"""
lignesConsole=['$ ls',
 'dir a',
 '14848514 b.txt',
 'dir d',
 '$ cd a']
 #'29116 f']
"""
source = Dossier("source")
#print(source.toString())

emplacementCourant = []
for ligne in lignesConsole:
    
    if ((ligne[2:4] == "cd")):
        #Change directory
        if (ligne[-2:] == ".."):
            #cd Retour
            emplacementCourant.pop()
            #print("Retour")
            
        else:
            #cd Repertoire
            emplacementCourant.append(ligne[5:])
            #print("Déplace :",ligne[5:])
        
    elif (ligne[:3] == "dir"):
        #Creer repertoire
        source.getSousDossier(emplacementCourant).ajouter(Dossier(ligne[4:]))
        #print("Créé :",ligne[4:],"dans",emplacementCourant)
        
    else:
        if (ligne[:4] != "$ ls"):
            #Creer fichier
            tailleFic = int(ligne.split(" ")[0])
            #print("Créé :", tailleFic,"dans",emplacementCourant,", le fichier avec comme contenu : ",source.getSousDossier(emplacementCourant)._contenu)
            #print("Créé :",tailleFic,"dans",emplacementCourant)
            source.getSousDossier(emplacementCourant).ajouter(tailleFic)
            
print(source)
print(source.sommeFichiers())
    
print("\n\n")
