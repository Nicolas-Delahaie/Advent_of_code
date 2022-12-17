fic = open("msg.txt", "r")
datas = fic.read()
fic.close()

cryptogramme=[]
#Str -> liste
for lettre in datas:
    cryptogramme.append(lettre)

def doublons(l):
    """Indique si la liste l contient des doublons"""
    nbElements = len(l)
    for i in range(nbElements-1):
        #Pour chaque element sauf le dernier
        for n in range(i+1, nbElements):
            if l[i] == l[n]:
                return True
    
def recherchePremierDifferent(cryptogramme, modulo=4):
    """Recherche le premier element du cryptogramme completant un mot de taille modulo avec chaque lettre distinctes"""
    iStart = 0      #Debut mot
    iEnd = modulo   #Fin mot
    while iEnd <= len(cryptogramme):
        chaine = cryptogramme[iStart:iEnd]
        if not doublons(chaine):
            return iEnd
        iStart +=1
        iEnd +=1


print(recherchePremierDifferent(cryptogramme))
print(recherchePremierDifferent(cryptogramme, 14))
