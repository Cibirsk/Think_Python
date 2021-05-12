def factoriel(n):
	if n == 0:
		return 1
	else:
		return n*factoriel(n-1)

#print(factoriel(5))


def fibonacci(n):
	if n<=1:
		return n
	else:
		return fibonacci(n-1)+fibonacci(n-2)

#print(fibonacci(6))

def count_down(number):
  if number <= 0:
    return
  print(number)
  count_down(number - 1)

def factorial(n):
    print("factorial has been called with n = " + str(n))
    if n == 1:
        print("factorial(1) renvoi 1")
        return 1
    else:
        res = n * factorial(n-1)
        print("intermediate result for ", n, " * factorial(" ,n-1, "): ",res)
        return res

#print(factorial(5))


def myFibo(n):
	if n==0:
		return 0
	elif n==1:
		return 1
	else:
		return myFibo(n-1)+ myFibo(n-2)

#print(myFibo(6))

def hanoi(n, source, helper, target):
    if n > 0:
        # move tower of size n - 1 to helper:
        hanoi(n - 1, source, target, helper)
        # move disk from source peg to target peg
        if source:
            target.append(source.pop())
        # move tower of size n-1 from helper to target
        hanoi(n - 1, helper, source, target)
        
source = [4,3,2,1]
target = []
helper = []
hanoi(len(source),source,helper,target)

print(source, helper, target)