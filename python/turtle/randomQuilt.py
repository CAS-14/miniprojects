from turtle import *
from random  import *

r = "0f"

a = Turtle()
a.speed(0)

while True:
    colorVal = ""
    for i in range(6):
        colorVal = colorVal+r[randint(0,1)]

    a.pencolor("#"+colorVal)
    a.fillcolor("#"+colorVal)

    a.pd()
    a.begin_fill()

    for i in range(4):
        a.fd(50)
        a.rt(90)

    a.end_fill()
    a.pu()

    a.rt(choice([-90, 0, 90, 180]))
    a.fd(50)
