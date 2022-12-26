fic = open(__file__ + "/../msg.txt", "r")
datas = fic.read()
fic.close()


class Map:
    def __init__(self, strDatas: str):
        strDatas = strDatas.split("\n")
        # relief, start
        self.relief = []
        dic = "abcdefghijklmnopqrstuvwxyz"
        for y in range(len(strDatas)):
            self.relief.append([])
            for x in range(len(strDatas[y])):
                case = strDatas[y][x]
                if case == "S":
                    height = 1
                    self.start = (x, y)
                elif case == "E":
                    height = 27
                    self.end = (x, y)
                else:
                    height = dic.index(case) + 1

                self.relief[-1].append(height)
        # Largeur, longueur
        self.larg = len(self.relief[0])
        self.long = len(self.relief)

    def __str__(self, currentPos = (-1, -1)):
        msg = ""
        for y in range(self.long):
            for x in range(self.larg):
                if currentPos[1] == y and currentPos[0] == x:
                    #Position courante
                    msg += " X "
                else:
                    msg += " "+str(self.relief[y][x])+" "
            msg += "\n"
        return msg        

    def getStepsToReachGoal(self):
        visitedBoxes = [
            [False for loop in range(self.larg)] for loop in range(self.long)
        ]
        visitedBoxes[self.start[1]][self.start[0]]
        etape = 0
        return self.browseBoxes(visitedBoxes, self.start, etape)

    def browseBoxes(self, visitedBoxes: list, currentPos: tuple, etape: int):
        etape += 1
        directions = ["U", "R", "D", "L"]
        etapesEnfants = []        
        for direction in directions:
            newPos = self.move(currentPos[0], currentPos[1], direction)
            if newPos != False:
                # La case adjacente existe
                if not visitedBoxes[newPos[1]][newPos[0]]:
                    # La nouvelle case n a pas encore ete visitee
                    actualRelief = self.relief[currentPos[1]][currentPos[0]]
                    newPosRelief = self.relief[newPos[1]][newPos[0]]
                    if newPosRelief <= actualRelief + 1:
                        # Case accessible
                        if newPosRelief == 27:
                            return etape
                        else:
                            # print("Etape numero", etape, "\n"+self.__str__(currentPos))
                            visitedBoxesCopy = visitedBoxes.copy()
                            visitedBoxesCopy[newPos[1]][newPos[0]] = True
                            etapesEnfants.append(self.browseBoxes(visitedBoxesCopy, newPos, etape))
        #Suppression des None
        while None in etapesEnfants:
            etapesEnfants.remove(None)

        if etapesEnfants == []:
            return None
        else:
            return min(etapesEnfants)

    def move(self, x, y, direction):
        """Retourne les coordonnees du nouveau point s'il ne sort pas de la map
        False sinon"""
        if direction == "U":
            y -= 1
            if y >= 0:
                newCoord = (x, y)
            else:
                newCoord = False
        elif direction == "R":
            x += 1
            if x < self.larg:
                newCoord = (x, y)
            else:
                newCoord = False
        elif direction == "D":
            y += 1
            if y < self.long:
                newCoord = (x, y)
            else:
                newCoord = False
        elif direction == "L":
            x -= 1
            if x >= 0:
                newCoord = (x, y)
            else:
                newCoord = False
        return newCoord

map = Map(datas)
# print(map)

map.getStepsToReachGoal()
