import turtle
import time
t=turtle.Pen()
turtle.speed("fastest")
turtle.pensize(2)
for x in range(100):
    t.forward(2*x)
    t.left(90)
    time.sleep(3)
