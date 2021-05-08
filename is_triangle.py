def is_triangle(a,b,c):
    if (a+b)>c:
        print("is triangle")
    else:
        print("not a triangle")

a=int(input('coté A: '))
b=int(input('coté B: '))
c=int(input('coté C: '))

is_triangle(a,b,c)
