
fic = open("messageADecoder.txt", "r")
datas = fic.read()
fic.close()

valeurs=datas.split("\n\n")
for n in range(len(valeurs)):
    valeurs[n] = valeurs[n].split("\n")
for lutin in range(len(valeurs)):
    for aliment in range(len(valeurs[lutin])):
        valeurs[lutin][aliment] = int(valeurs[lutin][aliment])
for lutin in range(len(valeurs)):
    somme = 0
    for aliment in range(len(valeurs[lutin])):
        somme += valeurs[lutin][aliment]
    valeurs[lutin] = somme
valeurs.sort()

print (valeurs[-1]+valeurs[-2]+valeurs[-3])

