from turtle import *

side = 10

while True:
    for i in range(3):
        fd(side)
        rt(120)

    lt(120)
    fd(side)
    rt(120)

    side *= 3
