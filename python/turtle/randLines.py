from turtle import *
from random import *

r = "0123456789abcdef"

v = Turtle()
v.speed(0)
v.pensize(10)

while True:
    colorVal = ""
    for i in range(6):
        colorVal = colorVal+r[randint(0,15)]

    v.pencolor("#"+colorVal)

    v.fd(randint(0, 100))
    v.rt(randint(0, 360))
