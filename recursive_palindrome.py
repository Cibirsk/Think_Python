#itérative function
def palindromeIter(word):
    for i in range(int(len(word)/2)):
        if word[i] != word[len(word)-1-i]:
            return False

    return True

#recursive function
def palindromeRecur(word):
    if len(word)==0:
        return True
    elif word[0]==word[-1]:
        return palindromeRecur(word[1:-1])
    else:
        return False

print(palindromeRecur('abcdtdcba'))


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