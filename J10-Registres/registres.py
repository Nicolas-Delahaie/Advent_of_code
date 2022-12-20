fic = open(__file__ +"/../msg.txt", "r")
datas = fic.read()
fic.close()

instructionsLines = datas.split("\n")
def lineToInstruction(instructionsLines):
    """Traduit des lignes d instructions en instruction
       De la forme (increment, nbEtapes)
       Exemples : naddx 5 donne (5, 2) car naddx prend 2 etapes pour agir"""
    instructions = []
    for i in range(len(instructionsLines)):

        if instructionsLines[i] == "noop":
            #Si c'est noop
            instructions.append((0,1))
        
        else:
            #Si c'est addx
            instructions.append((int(instructionsLines[i][5:]),2))
    return instructions
instructions = lineToInstruction(instructionsLines)

X = [1]

def readInstructions(X, instructions):
    for instruction in instructions:
        # print("Etape :",len(X),"Valeur de X :",X[len(X)-1],"Instruction :",instruction[0],"\n")
        for loop in range(instruction[1]-1):
            #Garde la meme valeur de registre
            X.append(X[-1])
            # print("Etape :",len(X),"Valeur de X :",X[len(X)-1],"Instruction :",instruction[0],"\n")
        #Modifie la valeur du registre
        X.append(X[-1]+instruction[0])

readInstructions(X, instructions)

def strenghtSum(X, a=40,b=20):
    cycle = b
    sum = 0
    for cycle in range(b, len(X), a):
        print("Cycle",cycle,":",cycle,"x",X[cycle-1])
        sum += cycle*X[cycle-1]
    return sum


strenghtSum = strenghtSum(X)
print(strenghtSum)



class Win:
    def __init__(self): 
        self.CRT = [["." for loop in range(40)] for loop in range(6)]
    def __str__(self):
        msg = ""
        for y in range(len(self.CRT)):
            for x in range(len(self.CRT[0])):
                msg += self.CRT[y][x]+" "
            msg += "\n"
        return msg
    def __repr__(self):
        return self.__str__()

    def allumer(self, spritePositions):
        width = len(self.CRT[0])
        height = len(self.CRT)

        for y in range(height):
            #Pour chaque ligne
            for x in range(width):
                #Pour chaque pixel/cycle
                cycle = y*width + x

                spritePos = spritePositions[cycle]
                if spritePos-1 <= x <= spritePos+1:
                    pixel = "#"
                else:
                    pixel = "."
                self.CRT[y][x] = pixel

w = Win()
print(w)
w.allumer(X)
print(w)
        

