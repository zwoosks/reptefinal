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
