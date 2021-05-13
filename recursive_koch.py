import turtle

#première version de la courbe de Koch
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

#autre version de la courbe Koch
def courbeVonKoch(t,n,cote) :
	if n == 0 :
		t.forward(cote)
	else :
		courbeVonKoch(t, n-1, cote/3)
		t.left(60)
		courbeVonKoch(t, n-1, cote/3)
		t.left(-120)
		courbeVonKoch(t, n-1, cote/3)
		t.left(60)
		courbeVonKoch(t, n-1, cote/3)

#flocon de Koch
def flocon(t):
    for i in range(3):
        courbeVonKoch(bob, 2, 100)
        t.left(-120)


bob = turtle.Turtle() #import module dans bob

#courbeVonKoch(bob, 2, 100)

flocon(bob)

#koch(bob, 100)

turtle.mainloop() # garde la fenêtre ouverte