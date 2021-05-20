def iteReverse(string):
    result=''
    longueur= len(string)-1
    while longueur > 0:
        result= string(longueur)
        longueur -= 1
    return result

print(iteReverse('tap'))