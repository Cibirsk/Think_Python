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

#def cartalk2():

def isPalindromic(word):
    response=False
    for i in range(len(word)):
        if word[i] == word[len(word)-1-i]:
            response=True
        else:
            response=False
    return response

print(isPalindromic('azerta'))
