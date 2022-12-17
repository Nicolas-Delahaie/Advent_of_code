fic = open("msg.txt", "r")
datas = fic.read()
fic.close()

donnees = datas.split("\n")


#Separation des caisses et des instructions
for i in range(len(donnees)):
    if donnees[i] == "":
        indiceSeparation = i

lignesCaisses = donnees[:indiceSeparation-1]
phrasesInstructions = donnees[indiceSeparation+1:]

#Re structuration des piles de caisses
pilesCaisses = []
nbPiles = int((len(lignesCaisses[0])-3)/4+1)
for i in range(nbPiles):
    #Pour chaque pile
    pilesCaisses.append([])

    for n in range(len(lignesCaisses)-1, -1, -1):
        #Pour chaque ligne
        indiceColonne = i*4+1
        elmt = lignesCaisses[n][indiceColonne]
        if  elmt != " ":
            pilesCaisses[i].append(elmt)

#Re structuration des instruction
for i in range(len(phrasesInstructions)):
    phrasesInstructions[i] = phrasesInstructions[i].split(" ")
instructions = []
for phraseInstruction in phrasesInstructions:
    for loop in range (int(phraseInstruction[1])):
        source = int(phraseInstruction[3])
        destination = int(phraseInstruction[5])
        instructions.append([source - 1, destination - 1])

#Deplacement des caisses
for instruction in instructions:
    source = instruction[0]
    destination = instruction[1]
    pilesCaisses[destination].append(pilesCaisses[source].pop())

#Affichage final
lettresQueue = []
for pile in pilesCaisses:
    lettresQueue.append(pile[-1])

print(''.join(lettresQueue))

