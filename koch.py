import turtle

def koch(t, n):
    """Draws a koch curve with length n."""
    if n < 20:
        t.fd(n)
        return
    n = n/3
    koch(t, n)
    t.lt(60)
    koch(t, n)
    t.rt(120)
    koch(t, n)
    t.lt(60)
    koch(t, n)

bob = turtle.Turtle() #import module dans bob
koch(bob, 200)
turtle.mainloop()