from turtle import *
from random import *

r = "0123456789abcdef"

x = Turtle()
x.speed(0)
x.pensize(3)

def triangle(side):
    for i in range(3):
        x.fd(side)
        x.rt(120)

def square(side):
    for i in range(4):
        x.fd(side)
        x.rt(90)

def pentagon(side):
    for i in range(5):
        x.fd(side)
        x.rt(72)

def hexagon(side):
    for i in range(6):
        x.fd(side)
        x.rt(60)

while True:
    x.pu()
    x.goto(randint(-700, 700), randint(-400, 400))
    x.rt(randint(-180, 180))

    colorVal = ""
    for i in range(6):
        colorVal = colorVal+r[randint(0,15)]
    x.pencolor("#"+colorVal)
    x.fillcolor("#"+colorVal)

    fill = randint(0,1)
    side = randint(10, 50)

    x.pd()
    if fill == 1: x.begin_fill()
    eval(choice(["triangle(side)", "square(side)", "pentagon(side)", "hexagon(side)", "x.circle(side)"]))
    if fill == 1: x.end_fill()
