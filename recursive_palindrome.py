#itérative function
def palindromeIte(word):
    for i in range(len (word)):
        if word[i] == word[len(word)-1-i]:
            return True
        else:
            return False


#recursive function
def palindromeRecu(word):
    if len(word)==0:
        return True
    elif word[0]==word[-1]:
        return palindrome(word[1:-1])
    else:
        return False

print(palindromeRecu('abcdtdcba'))


#version corrigé du livre
def first(word):
    """Returns the first character of a string."""
    return word[0]

def last(word):
    """Returns the last of a string."""
    return word[-1]

def middle(word):
    """Returns all but the first and last characters of a string."""
    return word[1:-1]

def is_palindrome(word):
    """Returns True if word is a palindrome."""
    if len(word) <= 1:
        return True
    if first(word) != last(word):
        return False
    return is_palindrome(middle(word))