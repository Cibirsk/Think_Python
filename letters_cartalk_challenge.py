
def readFile():
    fin = open('words2.txt') #open the file
    for word in fin:
        cartalk1(word)

def cartalk1(word):
        i=0
        theWord= word
        while i < len(theWord)-1:
            if word[i]==theWord[i+1] and theWord[i+2]==theWord[i+3] and theWord[i+4]==theWord[i+5]:
                print(theWord)
            else:
                theWord = theWord[i+1:]
                print(theWord)
            i +=1

readFile()
