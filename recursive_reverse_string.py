#iterative version
def iteReverse(string):
    result=''
    longueur= len(string)-1
    while longueur >= 0:
        result= result + string[longueur]
        longueur -= 1
    return result

#recursive version
def reverseString(string):
    # Base Case
    if len(string) == 0:
        return string

    # Recursive Case
    else:
        return reverseString(string[1:]) + string[0]

print(reverseString('abcde'))