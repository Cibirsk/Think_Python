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

#“I was driving on the highway the other day and I happened to notice my odometer.
#Like most odometers, it shows six digits, in whole miles only. So, if my car had 300,000
#miles, for example, I’d see 3-0-0-0-0-0.
#“Now, what I saw that day was very interesting. I noticed that the last 4 digits were
#palindromic; that is, they read the same forward as backward. For example, 5-4-4-5 is a
#palindrome, so my odometer could have read 3-1-5-4-4-5.
#“One mile later, the last 5 numbers were palindromic. For example, it could have read
#3-6-5-4-5-6. One mile after that, the middle 4 out of 6 numbers were palindromic. And
#you ready for this? One mile later, all 6 were palindromic!
#“The question is, what was on the odometer when I first looked?”
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

#“Recently I had a visit with my mom and we realized that the two digits that make
#up my age when reversed resulted in her age. For example, if she’s 73, I’m 37. We
#wondered how often this has happened over the years but we got sidetracked with other
#topics and we never came up with an answer.
#“When I got home I figured out that the digits of our ages have been reversible six times
#so far. I also figured out that if we’re lucky it would happen again in a few years, and
#if we’re really lucky it would happen one more time after that. In other words, it would
#have happened 8 times over all. So the question is, how old am I now?”
#Write a Python program that searches for solutions to this Puzzler. Hint: you might find the string
#method zfill useful.
def reverse(numb):
    reverseNumb=''
    reverseNumb +=numb[1:]
    reverseNumb +=numb[:1]
    return reverseNumb
#zfill rempli de 0 pour avoir un nombre à 2 chiffre si inférieur à 10 (ex: 05)
def cartalk3():
    for mother in range(36,99):
        for son in range(18,99):
            if reverse(str(son).zfill(2)) == str(mother).zfill(2) and (mother-son)>18 and (mother-son)<37:
                print(str(son).zfill(2) + '  ' + str(mother).zfill(2))

cartalk3()


