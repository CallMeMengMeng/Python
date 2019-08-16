#输入某年某月某日，判断这一天是这一年的第几天？
#-*-coding:utf-8-*-
year=int(input("Please input year: \n"))
month=int(input("Please input month: \n"))
day=int(input("Please input day: \n"))

month1=[0,31,60,91,121,152,182,213,244,274,305,335,366]
month2=[0,30,59,90,120,151,181,212,243,273,304,334,365]

if ((year%400==0)and(year%100==0)) or ((year%100!=0)and(year%4==0)):
	Day=month1[month-1]+day
else:
		Day=month2[month-1]+day
		
print("It's the %sth day of the year." %Day)
