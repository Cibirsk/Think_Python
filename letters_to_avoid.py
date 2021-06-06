#find words without forbidden letters in a file
def avoid():
    fin = open('words.txt') #open the file
    lettersOvoid = input(' Letters to avoid: ')
    countWord=0
    for line in fin:
        countWord +=1
        for letter in lettersOvoid:
            if letter in line:
                countWord -=1
                break
    return countWord

#returns True if the word contains only letters in the list
def useOnly(word, lettersList):
    response=False
    for letter in word:
        if letter in lettersList:
            response=True
        else:
            response=False
    return response

#returns True if the word uses all the required letters at least once
def use_all(letters_list):
    fin = open('words2.txt') #open the file
    countWord=0
    for line in fin:
        for letter in letters_list:
            if letter in line:
                countWord +=1
            else:
                countWord -=1
    return countWord

print(use_all('ir'))

