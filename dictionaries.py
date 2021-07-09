#compte le nombre de fois qu'une lettre apparait dans 1 string
def checkString(s):
        listLetters={}
        for c in s:
                if c not in listLetters:
                        listLetters[c]=1
                else:
                        listLetters[c] +=1
        return listLetters

def checkString2(s):
        listLetters={}
        for c in s:
                a=listLetters.get



g={'marque':'aston',
'modèle':'DB7',
'année':1967}
print(g.get('modèle','none'))