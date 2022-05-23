import turtle

v = turtle.Turtle()
v.speed(6)

# move to start and blue color
v.penup()
v.goto(0, -125)
v.pencolor("dodgerblue")
v.fillcolor("dodgerblue")
v.pendown()

# circle
v.speed(10)
v.begin_fill()
v.circle(150)
v.end_fill()
v.speed(6)

# move to "h" and white color
v.penup()
v.goto(-55, 205)
v.pencolor("black")
v.fillcolor("white")
v.pendown()

# letter "h"
v.begin_fill()
v.right(105)
v.forward(260)
v.left(105)
v.forward(33)
v.left(75)
v.forward(125)
v.right(75)
v.forward(25)
v.right(105)
v.forward(125)
v.left(105)
v.forward(33)
v.left(75)
v.forward(125)
v.speed(0)
for i in range(10):
    v.forward(3)
    v.left(10)
v.forward(1.5)
v.left(5)
v.speed(6)
v.forward(37.5)
v.right(105)
v.forward(110)
v.left(105)
v.forward(33)
v.end_fill()

# move to "p"
v.penup()
v.goto(-25, -140)
v.pendown()

# letter "p"
v.right(105)
v.forward(246)
v.right(75)
v.forward(70.5)
v.speed(0)
for i in range(10):
    v.forward(3)
    v.right(10)
v.forward(1.5)
v.right(5)
v.speed(6)
v.forward(37.5)
v.forward(76)
v.speed(0)
for i in range(7):
    v.forward(3)
    v.right(10)
v.forward(1.5)
v.right(5)
v.speed(6)
v.forward(47.5)
v.left(75)
v.forward(97)
v.right(75)
v.forward(35)
v.end_fill()

v.hideturtle()
turtle.done()
