#Four numbers: 1, 2, 3, 4 can consist three-bit-numbers
#-*-coding: utf-8-*-
for i in range(1,5):
    for j in range(1,5):
        for k in range(1,5):
            if i!=j and j!=k and k!=i:
                print (i,j,k)
