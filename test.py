def both(word1,word2):
    for letter in word1:
        if letter in word2:
            print(letter)

both('abcdef', 'cf')