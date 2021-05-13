#fonction d'Ackermann

#  si m = 0, alors A(0, n) = n+1,
#  sinon si n=0, A(m, 0) = A(m-1, 1)
#  sinon A(m, n) = A(m-1, A(m, n-1))

def ack(m,n):
    if m == 0:
        return n+1
    elif n == 0:
        return ack(m-1,1) 
    else:
        return ack(m-1, ack(m,n-1))

print(ack(3,4)) #résultat 125
