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
    polygon(bob,long,n)

def circle(t,r):
    circonference=2*r*3.14
    n=1
    length=circonference/n
    for i in range(n):
        t.fd(length)
        t.lt(360/n)

import turtle
t=turtle.Turtle()
circle(t,10)

