import turtle

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

def flocon(t):
    for i in range(3):
        courbeVonKoch(bob, 2, 100)
        t.left(-120)


bob = turtle.Turtle() #import module dans bob
#courbeVonKoch(bob, 2, 100)
flocon(bob)

turtle.mainloop()