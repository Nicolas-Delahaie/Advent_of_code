# -*- coding: utf-8 -*-
"""
Created on Mon Dec 12 09:52:47 2022

@author: nico6
"""

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
    nbDepl = int(phraseInstruction[1])
    source = int(phraseInstruction[3])
    destination = int(phraseInstruction[5])
    instructions.append([nbDepl, source - 1, destination - 1])


#Deplacement des caisses
for instruction in instructions:
    nbDepl = instruction[0]
    source = instruction[1]
    destination = instruction[2]
    
    blocADeplacer = pilesCaisses[source][-nbDepl:]
    for loop in range(nbDepl):
        pilesCaisses[source].pop()
    
    for caisse in blocADeplacer:
        pilesCaisses[destination].append(caisse)

#Affichage final
lettresQueue = []
for pile in pilesCaisses:
    lettresQueue.append(pile[-1])

print(''.join(lettresQueue))

