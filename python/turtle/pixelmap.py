import turtle
from random import *

angle = [90, 270]
dist = [5, 10, 15, 20]
m = turtle.Turtle()
m.speed(1000)

while True:
    m.forward(choice(dist))
    m.rt(choice(angle))
