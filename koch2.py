import turtle

def Koch(  n, cote  ) :
	if n == 0 :
		tl.forward(cote)
	else :
		courbeVonKoch(n-1, cote/3)
		tl.left(60)
		courbeVonKoch(n-1, cote/3)
		tl.left(-120)
		courbeVonKoch(n-1, cote/3)
		tl.left(60)
		courbeVonKoch(n-1, cote/3)

bob = turtle.Turtle() #import module dans bob
koch(bob, 200)
turtle.mainloop()