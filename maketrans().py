import sys
for i in range(0,5):
    intab="abcdefghijklmnopqrstuvwxyz"
    outtab="cdefghijklmnopqrstuvwxyzab"
    transtab=str.maketrans(intab,outtab)    
    print('Please enter a string:')
    str=str(sys.stdin.readline())
    print(str.translate(transtab))
