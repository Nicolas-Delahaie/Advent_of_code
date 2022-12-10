dic = list("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ")

fic = open("msg.txt", "r")
datas = fic.read()
fic.close()

sacs = datas.split("\n")


#Decoupage par paquets de 3
equipes = []
for i in range(0, len(sacs), 3):
    equipes.append([])
    for n in range(3):
        equipes[-1].append(sacs[i+n])

def reinitialiserCompteur(compteur):
    for lettre in dic:
        compteur[lettre] = 0

#Comptage de lettres
lettresCommunes = []
compteurEquipe = {}
compteurElfe = {}
for equipe in equipes:
    reinitialiserCompteur(compteurEquipe)
    #Compte le nombre de lettre de chaque elfe d une equipe
    for elfe in equipe:
        reinitialiserCompteur(compteurElfe)
        #Met 1 a la lettre lorsquelle est la
        for lettre in elfe:
            compteurElfe[lettre] = 1
        #Fusionne le compteur de l elfe au compteur de l equipe
        for lettre in compteurElfe:
            compteurEquipe[lettre] +=compteurElfe[lettre]

    #Regarde si une lettre est dans les 3 elfes
    for lettre in compteurEquipe:
        if compteurEquipe[lettre] == 3:
            lettresCommunes.append(lettre)
            print (lettre)

#Transformation des lettres en priorites
priorites = []
for lettre in lettresCommunes:
    priorites.append(dic.index(lettre)+1)
print(sum(priorites))


