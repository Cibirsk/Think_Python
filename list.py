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
