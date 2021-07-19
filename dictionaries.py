#compte le nombre de fois qu'une lettre apparait dans 1 string
from list import has_duplicates


def checkString(s):
        listLetters={}
        for c in s:
                if c not in listLetters:
                        listLetters[c]=1
                else:
                        listLetters[c] +=1
        return listLetters


myCar={'marque':'aston',
'modèle':'DB5',
'année':1964,
'couleur':'grey'}


def dicoLoop(h):
        for c in h:
                print(c,h[c])
        for c in h:
                print(c)

def invert_dict(d):
        inverse = {}
        for key in d:
                val = d[key]
                if val not in inverse:
                        inverse[val] = [key]
                else:
                        inverse[val].append(key)
        return inverse


known = {0:0, 1:1}
def fibonacci(n):
        if n in known:
                return known[n]
        res = fibonacci(n-1) + fibonacci(n-2)
        known[n] = res
        return res


"""
Write a function that reads the words in words.txt and stores them as keys in a
dictionary. It doesn’t matter what the values are. Then you can use the in operator as a fast way to
check whether a string is in the dictionary.
"""
def checkDico(w):
        fin=open('words2.txt')
        myDico={}
        for word in fin:
                myDico[word.strip()]=''
        if w in myDico:
                return True
        else:
                return False

#renvoie dictionnaire inversé
def invert_dict(d):
        inverse = {}
        for key in d:
                if d[key] not in inverse:
                        inverse[d[key]] = [key]
                else:
                        inverse[d[key]].append(key)
        return inverse

#version avec setdefault
def invert_dict2(d):
        inverse = {}
        for key in d:
                inverse.setdefault(d[key],key)
        return inverse

"""
If you did Exercise 10.7, you already have a function named has_duplicates that
takes a list as a parameter and returns True if there is any object that appears more than once in the
list.
Use a dictionary to write a faster, simpler version of has_duplicates
"""
test_list=['lapin','cheval','chien','chat','cheval']

def has_duplicate2(the_liste):
        tempDic={}
        for i in the_liste:
                if i not in tempDic:
                        tempDic[i]=''
                else:
                        return True

        return False

print(has_duplicate2(test_list))
