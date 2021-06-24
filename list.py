"""
Write a function called nested_sum that takes a list of lists of integers and adds up
the elements from all of the nested lists. For example:
>>> t = [[1, 2], [3], [4, 5, 6]]
>>> nested_sum(t)
21
"""
t = [[1, 2], [3], [4, 5, 6]]

def nested_sum(myList):
    mySum=0
    for t1 in myList:
        for t2 in t1:
            mySum += t2
    return mySum


"""
Write a function called cumsum that takes a list of numbers and returns the cumulative
sum; that is, a new list where the ith element is the sum of the first i + 1 elements from the
original list. For example:
>>> t = [1, 2, 3]
>>> cumsum(t)
[1, 3, 6]
"""
def cumsum(myList):
    result=[]
    for i in range(len(myList)):
       result.append((sum(myList[0:i+1])))
    return result    


"""
Write a function called middle that takes a list and returns a new list that contains
all but the first and last elements. For example:
>>> t = [1, 2, 3, 4]
>>> middle(t)
[2, 3]
"""
def middle(myList):
    return myList[1:-1]


"""
Write a function called chop that takes a list, modifies it by removing the first and
last elements, and returns None. For example:
>>> t = [1, 2, 3, 4]
>>> chop(t)
>>> t
[2, 3]
"""
def chop(myList):
    global t #créé t en tant que variable globale
    myList=myList[1:-1]
    t=myList

"""
Write a function called is_sorted that takes a list as a parameter and returns True
if the list is sorted in ascending order and False otherwise. For example:
>>> is_sorted([1, 2, 2])
True
>>> is_sorted(['b', 'a'])
False
"""

def is_sorted(myList):
    tempList=[]
    tempList.extend(myList)
    myList.sort()
    if tempList==myList:
        return True
    else:
        return False


"""
Two words are anagrams if you can rearrange the letters from one to spell the other.
Write a function called is_anagram that takes two strings and returns True if they are anagrams.
"""
def is_anagram(firStr,secStr):
    if len(firStr) != len(secStr):
        return False
    for i in firStr:
        if i not in secStr:
            return False
    return True


"""
Write a function called has_duplicates that takes a list and returns True if there
is any element that appears more than once. It should not modify the original list.
"""
def has_duplicates(myList):
    tempList=[]
    for i in myList:
        if i not in tempList:
            tempList.append(i)
        else:
            return False
    return True


"""
This exercise pertains to the so-called Birthday Paradox, which you can read about
at http: // en. wikipedia. org/ wiki/ Birthday_ paradox .
If there are 23 students in your class, what are the chances that two of you have the same birthday?
You can estimate this probability by generating random samples of 23 birthdays and checking for
matches. Hint: you can generate random birthdays with the randint function in the random
module.
You can download my solution from http: // thinkpython2. com/ code/ birthday. py .
"""

def birthday_paradox():
    import random
    j=1
    tauxPositif=0
    while j<10000:

        birth_list=[]
        same_date=0 #stocke les cas avec 2 dates identiques
        i=1
        while i <= 23:
            date=random.randint(1,365)

            if date in birth_list:
                same_date +=1
            birth_list.append(date)

            i +=1

        if same_date > 0:
            tauxPositif +=1 #additionne le nombre de cas avec date identique sur l'ensemble des essais
        j +=1

    pourCentTaux= (tauxPositif/10000)*100
    print(pourCentTaux)

"""
Write a function that reads the file words.txt and builds a list with one element
per word. Write two versions of this function, one using the append method and the other using
the idiom t = t + [x]. Which one takes longer to run? Why?
Solution: http: // thinkpython2. com/ code/ wordlist. py .
"""
def wordList():
    theList=[]
    fin = open('words.txt') #open the file
    for word in fin:
        for i in word[0:1]:
            theList.append(i)
    print(theList)

wordList()

