import time
t=time.time()


nbrHeur=t//3600
nbrMin=(t%60)//60
nbrSec=t%3600

nbrJour= t//(3600*24)

print('heures: ' + str(nbrHeur))
print('minutes: ' + str(nbrMin))
print('secondes: ' + str(nbrSec))
print('jours depuis epoch: ' + str(int(nbrJour)))
