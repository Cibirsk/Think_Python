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

def petale(t,r):
    arc(t,r,90)
    bob.lt(90)
    arc(t,r,90)

def flower(t,r):
    for i in range(16):
        petale(t,r)
        bob.lt(360/16)

bob = turtle.Turtle() #import module dans bob

radius = 100 #longueur de l'arc


flower(bob,radius)

# wait for the user to close the window
turtle.mainloop()