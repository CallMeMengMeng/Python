import math
a = input('A类不确定度：')
b = input('B类不确定度：')
u=math.sqrt(a**2+b**2)
t=float(u)
print("合成不确定度为:%s" %u)
