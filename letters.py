import math
import turtle

def polyline(t, n, length, angle):
    """Draws n line segments.

    t: Turtle object
    n: number of line segments
    length: length of each segment
    angle: degrees between segments
    """
    for i in range(n):
        t.fd(length)
        t.lt(angle)

def arc(t, r, angle):
    """Draws an arc with the given radius and angle.

    t: Turtle
    r: radius
    angle: angle subtended by the arc, in degrees
    """
    arc_length = 2 * math.pi * r * abs(angle) / 360
    n = int(arc_length / 4) + 3
    step_length = arc_length / n
    step_angle = float(angle) / n

    # making a slight left turn before starting reduces
    # the error caused by the linear approximation of the arc
    t.lt(step_angle/2)
    polyline(t, n, step_length, step_angle)
    t.rt(step_angle/2)

bob = turtle.Turtle() #import module dans bob

radius = 100 #longueur de l'arc

def draw_a(t):
    t.lt(60)
    t.fd(100)
    t.rt(120)
    t.fd(100)
    t.lt(180)
    t.fd(50)
    t.lt(60)
    t.fd(50)

def draw_b(t):
    t.lt(90)
    t.fd(100)
    t.bk(100)
    t.rt(90)
    arc(t,25,180)
    t.rt(180)
    arc(t,25,180)

def draw_c(t):
    arc(t,100,20)
    t.up()
    arc(t,100,140)
    t.down()
    arc(t,100,200)

def spirale(t):
    


spirale(bob)

# wait for the user to close the window
turtle.mainloop()