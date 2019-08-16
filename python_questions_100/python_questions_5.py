#输入三个整数，比较三个数的大小并以小到大输出结果
#-*-coding:utf-8-*-
num1=int(input("Please enter the first number: \n"))
num2=int(input("Please enter the second number: \n"))
num3=int(input("Please enter the third number: \n"))

l=[num1,num2,num3]
l.sort()
print("The result is: %s" %l)

