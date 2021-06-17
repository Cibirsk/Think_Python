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
