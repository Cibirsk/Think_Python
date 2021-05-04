"""
import turtle
bob = turtle.Turtle()
for i in range(4):
    bob.fd(100)
    bob.lt(90)

turtle.mainloop()
"""

def square(t,length):
    for i in range(4):
        t.fd(length)
        t.lt(90)

def polygon(t,length,n):
    for i in range(n):
        t.fd(length)
        t.lt(360/n)

def myBob(long,n):
    import turtle
    bob= turtle.Turtle()
    #square(bob,long)
    polygon(bob,long,n)

def circle(t,r):
    # long=1
    # nbr côtés= 2*3.14*r
    # circonférence=
    for i in range():
        t.fd()
        t.lt(360/n)


myBob(30, 5)

#n= nombre de côtés

#circonférence= 2* 3.14* r