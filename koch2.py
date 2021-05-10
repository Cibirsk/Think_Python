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

bob = turtle.Turtle() #import module dans bob
courbeVonKoch(bob, 2, 100)
turtle.mainloop()