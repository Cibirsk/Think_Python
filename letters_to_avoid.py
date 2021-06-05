#find words without forbidden letters in a file
fin = open('words2.txt')

#    for line in fin:

def avoid():
    lettersOvoid = input(' Letters to avoid: ')
    countWord=0
    for line in fin:
        countWord +=1
        if lettersOvoid in line:
            countWord -=1
    return countWord

print(avoid())