from tkinter import *
import random
tk=Tk()
canvas=Canvas(tk,width=400,height=400)
canvas.pack()
def random_triangle(width,height):
    x1=random.randrange(width)
    y1=random.randrange(height)
    x2=x1+random.randrange(width)
    y2=y1+random.randrange(height)
    x3=x2+random.randrange(width)
    y3=y2+random.randrange(height)
    canvas.create_polygon(x1,y1,x2,y2,x3,y3)
random_triangle(400,400)
for x in range(0,100):
    random_triangle(400,400)
    
    
