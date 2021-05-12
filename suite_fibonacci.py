def fibonacci(n):
	if n<=1:
		return n #je retourne n pour n qui renvoie 0 et qui renvoie 1
	else:
		return fibonacci(n-1)+fibonacci(n-2)


#autre version
def myFibo(n):
	if n==0:
		return 0 # premier terme de la suite
	elif n==1:
		return 1 # second terme de la suite
	else:
		return myFibo(n-1)+ myFibo(n-2)