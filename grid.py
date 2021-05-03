#faire un carré composé de 4 rangs et 4 colonnes
def plusMoins():
    print('+ - - - - ', end=' ')

def plusFin():
    print('+')

def baton():
    print('|         ', end=' ')

def batonFin():
    print('|')

def lignePleine():
    doTwice(plusMoins)
    plusFin()

def ligneVide():
    doTwice(baton)
    batonFin()

def doTwice(f):
    f()
    f()

def doFour(f):
    doTwice(f)
    doTwice(f)

def grandLignePleine():
    doFour(plusMoins)
    plusFin()

def grandLigneVide():
    doFour(baton)
    batonFin()

def firstRow(): #un rang en entier
    grandLignePleine()
    doFour(grandLigneVide)

doFour(firstRow)



