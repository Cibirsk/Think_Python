"""
A number, a, is a power of b if it is divisible by b and a/b is a power of b. 
Write a function called is_power that takes parameters a and b 
and returns True if a is a power of b. 
Note: you will have to think about the base case.
"""
#code faux, la récursive ne fonctionne pas
def isPower(a,b):
    if a%b == 0:
        if isPower(a/b, b):
            return True
    
        else:
            return False

#code correct avec recursive
def is_power(a, b):
    """Checks if a is power of b."""
    if a == b:
        return True
    elif a%b == 0:
        return is_power(a/b, b)
    else:
        return False

a=4
b=2
print (isPower(a,b))
print(is_power(a,b))
