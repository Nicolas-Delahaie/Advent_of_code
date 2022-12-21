from math import *  # Pour floor

fic = open(__file__ + "/../msgTest.txt", "r")
datas = fic.read()
fic.close()

strMonkeys = datas.split("\n\n")


class MonkeyPack:
    def __init__(self, strMonkeys):
        """Necessite des singes en str"""
        for i in range(len(strMonkeys)):
            strMonkeys[i] = strMonkeys[i].split("\n")

        self.monkeys = []
        for strMonkey in strMonkeys:
            self.monkeys.append(Monkey(strMonkey))

    def __str__(self):
        msg = "Horde de singes :\n"
        for monkey in self.monkeys:
            msg += " - " + monkey.__str__() + "\n"
        return msg

    def __repr__(self):
        return self.__str__()

    def getMonkey(self, index):
        return self.monkeys[index]

    def getPackLevel(self):
        levels = [
            self.getMonkey(i).inspectedItemsNumber for i in range(len(self.monkeys))
        ]
        levels.sort()
        return levels[-1] * levels[-2]

    def getPPCM(self):
        dividers = []
        for i in range(len(self.monkeys)):
            dividers.append(self.getMonkey(i).divider)
        ppcm = 1
        for divider in dividers:
            ppcm *= divider
        return ppcm

    def takeARide(self, worryDecreaseRatio):
        """1 tour : Chaque singe joue avec chaque objet et les transmet en consequent"""
        ppcm = self.getPPCM()
        for monkey in self.monkeys:
            while monkey.isPlaying():
                monkey.inspectLastItem(self, worryDecreaseRatio, ppcm)


class Monkey:
    def __init__(self, strMonkey):
        itemsStr = strMonkey[1][18:].split(", ")
        self.items = []
        for itemstr in itemsStr:
            self.items.append(Item(int(itemstr)))
        self.operation = (strMonkey[2][23], strMonkey[2][25:])
        self.divider = int(strMonkey[3][21:])
        self.linkedMonkeys = (int(strMonkey[4][29]), int(strMonkey[5][30]))
        self.inspectedItemsNumber = 0

    def __repr__(self):
        return self.__str__()

    def __str__(self):
        msg = (
            "Singe ayant inspecté "
            + str(self.inspectedItemsNumber)
            + " objets. Il possede :"
        )
        for i in range(len(self.items)):
            msg += str(self.items[i]) + " "
        msg += (
            ". Il est lié aux singes "
            + str(self.linkedMonkeys[0])
            + " et "
            + str(self.linkedMonkeys[1])
        )
        return msg

    def inspectLastItem(self, hisPack, worryDecreaseRatio, packPPCM):
        """Inspecte un objet et le transmet"""
        item = self.items[0]
        # Joue avec l objet -> multiplication de la valeur
        if self.operation[0] == "+":
            # Addition
            item.worryLvl += int(self.operation[1])
        else:
            # Multiplication
            if self.operation[1] == "old":
                # Multiplier par lui meme = au carre
                item.worryLvl *= item.worryLvl
            else:
                # Multiplier par un entier
                item.worryLvl *= int(self.operation[1])
        # Reduit le stress
        item.worryLvl %= packPPCM

        # Finit de jouer -> stress diminue
        item.worryLvl = floor(item.worryLvl / worryDecreaseRatio)

        # Se lasse -> donne l objet
        if item.worryLvl % self.divider == 0:
            # Divisible -> envoie au premier singe lie
            self.throwTo(hisPack.getMonkey(self.linkedMonkeys[0]))
        else:
            # Non divisible -> envoie au deuxieme singe lie
            self.throwTo(hisPack.getMonkey(self.linkedMonkeys[1]))

        # Augmente son score
        self.inspectedItemsNumber += 1

    def throwTo(self, monkey):
        """Donne le premier objet a monkey"""
        monkey.items.append(self.items.pop(0))

    def isPlaying(self):
        """Indique si le singe a encore un objet"""
        if self.items == []:
            return False
        else:
            return True


class Item:
    def __init__(self, worryLvl):
        self.worryLvl = worryLvl

    def __repr__(self):
        return self.__str__()

    def __str__(self):
        return str(self.worryLvl)


monkeys = MonkeyPack(strMonkeys)
print(monkeys)
worryDecreaseRatio = 1
for loop in range(10000):
    monkeys.takeARide(worryDecreaseRatio)
print(monkeys)
print("Score de la horde :", monkeys.getPackLevel())
