import turtle

def koch(t, n):
    """Draws a koch curve with length n."""
    if n < 20:
        t.fd(n)
        return
    n = n/3
    koch(t, n) # koch 1
    t.lt(60)
    koch(t, n) # koch 2
    t.rt(120)
    koch(t, n) # koch 3
    t.lt(60)
    koch(t, n) # koch 4

bob = turtle.Turtle() #import module dans bob
koch(bob, 100)
turtle.mainloop()