#一个整数，它加上100后是一个完全平方数，再加上168又是一个完全平方数，请问该数是多少？
#-*-coding: utf-8-*-
for m in range(168):
    for n in range(m):
        if (m+n)*(m-n)==168:
            x=n**2-268
            print("x的取值可能为：%s" %x)
            
