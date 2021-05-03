def plusMoins():
    print('+ - - - - ', end=' ')

def plusFin():
    print('+')

def baton():
    print('|         ', end=' ')

def batonFin():
    print('|')

def lignePleine():
    doTwice(plusMoins())
    plusFin()

def ligneVide():
    doTwice(baton())
    batonFin()

def doTwice(f):
    f()
    f()

def doFour(f):
    doTwice(f)
    doTwice(f)

def grid()