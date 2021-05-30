import math

def factorial(n):
    if n == 0:
        return 1
    return factorial(n-1)*n

def estimate_pi():
    k=0
    total=0
    factor= (2* math.sqrt(2))/9801
    
    while True:
        num= factorial(4*k) * (1103+ (26390 * k))
        den= (factorial(k)**4) * (396**(4*k))
        temp= factor * num/den
        total += temp
        k +=1
        if temp < 1e-15:
            break 
    
    return 1/total

print(estimate_pi())








