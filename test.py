def iteReverse(string):
    result=''
    longueur= len(string)-1
    while longueur >= 0:
        result= result + string[longueur]
        longueur -= 1
    return result

a='tap'
#print(iteReverse(a))

def recuReverse(string):
    if len(string) == 0:
        return string[longueur]
    else:
        return recuReverse(string[longueur-1])
        
def reverseString(string):
    # Base Case
    if len(string) == 0:
        return string

    # Recursive Case
    else:
        return reverseString(string[1:]) + string[0]

print(reverseString('tapir'))