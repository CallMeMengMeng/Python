from tkinter import *
import random
import time
tk=Tk()
canvas=Canvas(tk,width=500,height=500)
canvas.pack()
def random_rectangle(width,height,fill_color):
    x1=random.randrange(width)
    y1=random.randrange(height)
    x2=x1+random.randrange(width)
    y2=y1+random.randrange(height)
    canvas.create_rectangle(x1,y1,x2,y2,fill=fill_color)
random_rectangle(400,400,"green")
random_rectangle(400,400,"red")
random_rectangle(400,400,"pink")
random_rectangle(400,400,"blue")
random_rectangle(400,400,"yellow")
random_rectangle(400,400,"orange")
random_rectangle(400,400,"purple")
time.sleep(2)
for x in range(0,400):
    random_rectangle(400,400)

