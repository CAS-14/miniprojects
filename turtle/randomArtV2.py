"""
randomArtV2.py copyright (c) 2020 by CAS.
This program will generate a field of random shapes in random colors.
"""

# setup
from turtle import *
from random import *
hexParts = "0123456789abcdef"
speed(0)
pensize(3)

# shape generation process
while True:

    # randomize position
    pu()
    goto(randint(-700, 700), randint(-400, 400))
    rt(randint(-180, 180))

    # randomize color
    colorVal = ""
    for i in range(6):
        colorVal = colorVal+hexParts[randint(0,15)]
    pencolor("#"+colorVal)
    fillcolor("#"+colorVal)

    if randint(0,1) == 1: begin_fill() # decides whether to fill shape or not

    # draw a random shape
    pd()
    side = randint(20,50)
    sides = randint(2,6)
    if sides == 2:
        circle(side)
    else:
        for i in range(sides):
            fd(side)
            rt(360/sides)

    end_fill() # finishes shape filling if it is supposed to be filled
