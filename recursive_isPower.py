"""
A number, a, is a power of b if it is divisible by b and a/b is a power of b. 
Write a function called is_power that takes parameters a and b 
and returns True if a is a power of b. 
Note: you will have to think about the base case.
"""
def isPower(a,b):
    if a%b == 0 and ((a/b)%b ==0):
        return True
    
    #isPower(a/b, b)

print(isPower(4,2))
"""
a%b == 0
a/b % b = 0
"""
