def check_fermat(a,b,c,n):
    if a**n + b**n == c**n:
        print('Fermat was wrong')
    else:
        print('He was right')


a=int(input('a: '))
b=int(input('b: '))
c=int(input('c: '))
n=int(input('n: '))
check_fermat(a,b,c,n)