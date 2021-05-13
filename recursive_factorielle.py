def factorial(n):
	if not isinstance(n,int): #test si n est un entier
		print("only for integer")
		return None
	elif n<0:
		print("only positive number")
		return None
	elif n==0:
		return 1
	else:
		return n * factorial(n-1)


print(factorial(4))