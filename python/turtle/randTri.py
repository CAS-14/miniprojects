from turtle import *
from random import *

r = "0123456789abcdef"

v = Turtle()
v.speed(0)
v.pensize(5)

while True:
    colorVal = ""
    for i in range(6):
        colorVal = colorVal+r[randint(0,15)]

    v.pencolor("#"+colorVal)
    v.fillcolor("#"+colorVal)

    dist = randint(-100,100)
    fill = randint(0,1)

    if fill == 1:
        v.begin_fill()

    for i in range(3):
        v.fd(dist)
        v.rt(120)

    if fill == 1:
        v.end_fill()

    v.pu()
    v.right(randint(-180, 180))
    v.fd(randint(-100,100))
    v.pd()
