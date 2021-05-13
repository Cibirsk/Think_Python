"""
A number, a, is a power of b if it is divisible by b and a/b is a power of b. 
Write a function called is_power that takes parameters a and b 
and returns True if a is a power of b. 
Note: you will have to think about the base case.
"""
def isPower(a,b):
    if a%b == 0:
        return True
    
    else:
        return False
    isPower(a/b, b)

def is_power(a, b):
    """Checks if a is power of b."""
    if a == b:
        return True
    elif a%b == 0:
        return is_power(a/b, b)
    else:
        return False

print (isPower(6,2))
print(is_power(6,2))
