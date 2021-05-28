#itérative function
def isPalindrome(word):
    for i in range(len (word)):
        if word[i] == word[len(word)-1-i]:
            return True
        else:
            return False


#recursive function
def palindrome(word):
    if word[0]== word[-1]:
        return palindrome(word[1:-1])
    else:
        return False

#print(isPalindrome('noon'))
#print(palindrome('noon'))
word='abcd'
print(word[1:-1])
