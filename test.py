def countdown(n):
    if n <=0:
        print("Blast")
    else:
        print(n)
        countdown(n-1)

def print_s(s,n):
    if n<=0:
        return
    else:
        print(s  + ' ' + str(n))
        print_s(s,n-1)

n=int(input("type a number: "))
print_s('top',n)