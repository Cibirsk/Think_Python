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

print(fibonacci(5))