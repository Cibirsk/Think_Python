def rotate_word(s,rot):
    s=s.lower()
    tempS=''
    for i in s:
        tempS += chr(ord(i)+rot)

    return tempS

#print(rotate_word('hal',1))
#print(rotate_word('cheer',7))

def find_rotate():
    fin = open('words2.txt')
    rotateDico={}
    for i in fin:
        for j in fin:
            for h in range(26):
                rotWord=rotate_word(j,h)
                if i.strip() == rotWord:
                    print('OK')

find_rotate()

#fin=open('words2.txt')
#for i in fin:
#    if i.strip() == 'hal':
#        print('ok')
#    else:
#        print('none')