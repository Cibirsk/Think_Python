def isPalindrome(word):
    for i in range(len (word)):
        if word[i] == word[len(word)-1-i]:
            return True
        else:
            return False


print(isPalindrome('noon'))
