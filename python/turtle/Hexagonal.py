import turtle

joe = turtle.Turtle()

size = 100

while size > 0:
    joe.circle(size, 360, 6)
    joe.lt(90)
    joe.pu()
    joe.fd(4)
    joe.rt(90)
    joe.pd()
    size -= 4

joe.hideturtle()

turtle.done()
