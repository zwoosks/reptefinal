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
        
def fullBoard(l):
    espais = 0
    for element in l:
        if element == " ":
            
def isAWonPlay(l, lletra):
    if eq(0, 4, 8, l, lletra) == True:
        return True
    elif eq(2, 4, 6, l, lletra) == True:
        return True
    elif eq(3, 4, 5, l, lletra) == True:
        return True
    elif eq(1, 4, 7, l, lletra) == True:
        return True
    elif eq(0, 3, 6, l, lletra) == True:
        return True
    elif eq(2, 5, 8, l, lletra) == True:
        return True
    else:
        return False
    
def eq(n1, n2, n3, l, lletra):
    if l[n1] == l[n2]:
        if l[n1] == l[n3]:
            if l[n1] == lletra:
                return True
    else:
        return False
            espais += 1
    if espais == 0:
        return True
    else:
        return False

def applyPlay(jug, l, lletra, n):
    print jug + " occupies position " + str(n)
    nova = l
    nova[n] = lletra
    return nova

def randomPlay(l):
    espais = []
    counter = 0
    for element in l:
        if element == " ":
            espais += [counter]
        counter += 1
    if len(espais) == 0:
        return -1
    else:
        return random.choice(espais)

def play(l):
    estat = True
    while estat == True:
        num = raw_input("Choose position to play (0-8): ")
        if disponible(l, int(num)) == True:
            return num
        else:
            "We are sorry. This position is not valid."
            
def disponible(l, n):
    if l[n] == " ":
        return True
    else:
        return False

def chooseLetterPlayer():
    estat = True
    while estat == True:
        lletra = raw_input("Choose between X or O: ")
        if lletra == "X":
            res = [lletra, "O"]
            return res
        elif lletra == "O":
            res = [lletra, "X"]
            return res
        else:
            print "We are sorry. This letter is not valid."
