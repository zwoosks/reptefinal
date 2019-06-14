import random
def chooseInitialPlayer():
    l = ["Player", "Computer"]
    return random.choice(l)

def startBoard():
    return [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
    
def drawBoard(l, n):
    if len(l) < 9:
        print "Error! Board badly designed!"
    else:
        print "Turn number: " + str(n)
        print "============"
        taula(l[6:9])
        print "------------"
        taula(l[3:6])
        print "------------"
        taula(l[0:3])
        print "============"

def taula(l):
    print "   |   |   "
    print " " + l[0] + " | " + l[1] + " | " + l[2] + " "
    print "   |   |   "

def isAFreeSpace(l, n):
    if l == [] or n >= 9:
        return False
    else:
        casella = l[n]
        if casella == " ":
            return True
        else:
            return False
