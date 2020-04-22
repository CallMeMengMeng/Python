import pyttsx3
import time
print("开始进行拼写，输入结束即停止程序")
print("拼写英文，请输入1")
print("拼写中文，请输入2")
temp=input("请输入选项:")
if temp=='1':
    wd=0
    trl=1
else:
    wd=1
    trl=0
f = open(r"english.txt",'r')        
line = f.readline()              
engine = pyttsx3.init()
content=[]
while line:
    line=str(line).strip()
    content.append(line.split('-'))
    line = f.readline()
f.close() 
 
while True:
    x=range(0,len(content))
    for i in x:
        engine.say(content[i][wd])
        time.sleep(5)
        engine.say(content[i][wd])
        engine.runAndWait()
        word=input("请拼写:")
        word=word.strip()
        if content[i][wd]==word:
            print("拼写正确")
        elif word=="结束":
            break
        else:
            print("拼写结束")    
        translate=input("请翻译:")
        translate=translate.strip()
        if content[i][trl]==translate:
            print("翻译正确")
        elif translate=="结束":
            break
        else:
             print("翻译错误")