# act25 logo

from turtle import *

# easily make square
def sq(col):
    fillcolor(col)
    pencolor(col)
    pendown()
    begin_fill()
    fd(50)
    rt(90)
    fd(100)
    rt(90)
    fd(50)
    rt(90)
    fd(100)
    end_fill()
    penup()
    rt(90)
    fd(60)

# squares
sq("orange")
sq("cyan")
sq("green")

# letters
pencolor("white")
rt(90)
fd(75)
rt(90)
fd(170)
write("A", font=("Courier", 50, "normal"))
back(60)
write("C", font=("Courier", 50, "normal"))
back(60)
write("T", font=("Courier", 50, "normal"))
back(50)
pencolor("black")
write("25", font=("Courier", 75, "normal"))

done()
