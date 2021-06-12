#find  words with three consecutive double letters
def cartalk1():
    fin = open('words2.txt') #open the file
    for word in fin:
        i=0
        while i < len(word)-1:
            if word[i]==word[i+1] and word[i+2]==word[i+3] and word[i+4]==word[i+5]:
                print(word)
                break
            i +=1

#find palindromic numbers in 6 numbers suite
# 1)      4 last palindromic, find this number
# 2)  +1  5 last palindromic
# 3)  +1  4 au the middle of 6 are palindromic
# 4)  +1  6 palindromic 

def isPalindromic(word):
    for i in range(int(len(word)/2)):
        if word[i] != word[len(word)-1-i]:
            return False

    return True

def cartalk2():
    for i in range(100000,1000000):
        km4Last=str(i)
        km5Last=str(i+1)
        km4Middle=str(i+2)
        km6=str(i+3)

        if isPalindromic(km4Last[2:]) and isPalindromic(km5Last[1:]) and isPalindromic(km4Middle[1:-1]) and isPalindromic(km6):
            print()
            print('Ce nombre respecte les conditions:')
            print('km4Last:   ' + km4Last)
            print('km5Last:   ' + km5Last)
            print('km4Middle: ' + km4Middle)
            print('km6:       ' + km6)

def reverse(numb):
    reverseNumb=''
    reverseNumb +=numb[1:]
    reverseNumb +=numb[:1]
    return reverseNumb

def cartalk3():
    for mother in range(36,99):
        for son in range(18,99):
            if reverse(str(son).zfill(2)) == str(mother).zfill(2) and (mother-son)>18 and (mother-son)<37:
                print(str(son).zfill(2) + '  ' + str(mother).zfill(2))

cartalk3()






