fin = open('words2.txt')

#    for line in fin:

def avoid():
    letters = input(' Letters to avoid: ')
    countWord=0
    for i in fin:
        countWord +=1
        for j in letters:
            if j==i:
                countWord -=1
                break
    return countWord

print(avoid())