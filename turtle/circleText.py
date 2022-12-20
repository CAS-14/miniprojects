from turtle import *

text = input("What word do you want in a circle? ")
deg = 360/len(text)

it = 0
pu()

for i in range(len(text)):
    it = it+1

    write(text[it-1], font=("Arial", 30, "normal"))
    circle(100, deg)

hideturtle()
done()
