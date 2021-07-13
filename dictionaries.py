#compte le nombre de fois qu'une lettre apparait dans 1 string
def checkString(s):
        listLetters={}
        for c in s:
                if c not in listLetters:
                        listLetters[c]=1
                else:
                        listLetters[c] +=1
        return listLetters


g={'marque':'aston',
'modèle':'DB7',
'année':1967,
'mon année':1967}

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

print(invert_dict(g))