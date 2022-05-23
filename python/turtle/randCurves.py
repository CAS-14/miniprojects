from turtle import *
from random import randint

r = "0123456789abcdef"

me = Turtle()
me.speed(0)
me.pensize(10)

while True:
    colorVal = ""
    for i in range(6):
        colorVal = colorVal+r[randint(0,15)]

    me.pencolor("#"+colorVal)

    me.circle(randint(0,50), randint(-180,180))

done()
