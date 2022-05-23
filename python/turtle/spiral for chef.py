# put comment here

import turtle

def main():
    toitle = turtle.Turtle()
    
    toitle.fillcolor("orange")
    toitle.begin_fill()

    for i in range(4):
        toitle.forward(100)
        toitle.right(90)

    toitle.end_fill()
    toitle.penup()
    toitle.forward(50)
    toitle.right(90)
    toitle.forward(50)
    
    toitle.pendown()
    toitle.fillcolor("ivory")
    toitle.begin_fill()

    for i in range(4):
        toitle.forward(100)
        toitle.left(90)

    toitle.end_fill()
    toitle.penup()
    toitle.forward(50)
    toitle.left(90)
    toitle.forward(25)
    
    toitle.pendown()
    toitle.write("Gavin", font=("Impact", 18, "bold"))
    toitle.hideturtle()
    
main()
turtle.done()
