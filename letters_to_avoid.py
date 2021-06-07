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
def useOnly(word, letterList):
    for letter in word:
        if letter not in letterList:
            return False
    return True


#returns True if the word uses all the required letters at least once
def use_all(letters_list):
    fin = open('words.txt') #open the file
    countWord=0
    tempCount=False
    for line in fin:
        for letter in letters_list:
            if letter in line:
                tempCount=True
            else:
                tempCount=False
                break #permet d'arrêter la recherche, sinon incremente même si faux avant
        if tempCount == True:
            countWord +=1
    return countWord

#returns True if the letters in a word appear in alphabetical order (double letters are ok)
def is_abecedarian(word):
    temp_word= word[1:]
    response=True
    for w,t in zip(word, temp_word):
        if w <= t :
            response= True 
        else:
            response= False
            break
    return response
