dic = list("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ")

fic = open("msg.txt", "r")
datas = fic.read()
fic.close()

sacs = datas.split("\n")

#Transformation str en list
for i in range(len(sacs)):
    sacs[i] = list(sacs[i])

#Decoupage en 2
for i in range(len(sacs)):
    sac = sacs[i]
    milieu = int(len(sac)/2)
    sacs[i] = []
    sacs[i].append(sac[:milieu])
    sacs[i].append(sac[milieu:])

#Recherche lettres en commun
lettresCommunes = []
for sac in sacs:
    lettreTrouvee = False;
    for i in range(len(sac[0])) :
        if not lettreTrouvee :
            for n in range(len(sac[1])):
                if (sac[0][i] == sac[1][n]) :
                    lettresCommunes.append(sac[0][i])
                    lettreTrouvee = True
                    break

#Transformation des lettres en priorites
priorites = []
for lettre in lettresCommunes:
    priorites.append(dic.index(lettre)+1)
print(sum(priorites))


