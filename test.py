def naturalNumb(a,b):
    if a>b:
        return
    else:
        print(a)
        naturalNumb(a+1,b)

#naturalNumb(3,10)

def printNaturalNumbers(lowerRange, upperRange) :
	if lowerRange <= upperRange :
	  print(lowerRange)
	  lowerRange += 1
	  helperFunction(lowerRange, upperRange)
	else :
		return

def helperFunction(lowerRange, upperRange) :
  if lowerRange <= upperRange :
    print(lowerRange)
    lowerRange += 1
    printNaturalNumbers(lowerRange, upperRange)
  else :
      return

# Driver Program 
n = 5
#printNaturalNumbers(1, n)

def printPattern(targetNumber) :
  
  if (targetNumber <= 0) :
    print(targetNumber)
    return

  print(targetNumber)
  printPattern(targetNumber - 5)
  print(targetNumber)

# Driver Program 
n = 10
printPattern(n)