def facto(n):
    result=0
    for i in range(n,1,-1):
        print(n)
        result=result + (n * (n-1))
    return result


def factorielle(n):
    if n==0:
        return 1
    else:
        return n*factorielle(n-1)


print('iteration: ' + str(facto(4)))
print('recursive: ' + str(factorielle(4)))