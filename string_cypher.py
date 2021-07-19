def rotate_word(s,rot):
    s=s.lower()
    tempS=''
    for i in s:
        tempS += chr(ord(i)+rot)

    return tempS

print(rotate_word('cheer',7))