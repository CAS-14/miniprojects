from turtle import *

x = 0

speed(0)
pensize(3)

col = "000001"

while True:
    pencolor("#"+col)
    circle(x, 30)

    x += 1

    col = str(int(col)+99)
    for i in range(6 - len(col)):
        col = "0"+col
