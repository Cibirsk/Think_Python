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
    circonference=2*r*3.14 # tour du disque
    n=50 #nombre de côté
    length=circonference/n # longeur de chaque pas
    for i in range(n):
        t.fd(length)
        t.lt(360/n)

def arc(t,r,angle):
    circonference=2*r*3.14
    length=(angle*2*r*3.14)/360
    n=50
    for i in range(n):
        t.fd(length/n)
        t.lt(angle/n)

import turtle
t=turtle.Turtle()

#circle(t,100) #t: turtle   100: rayon du cercle

arc(t,100,180)
turtle.mainloop()

