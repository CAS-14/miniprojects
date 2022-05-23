'''
Put your comment here
'''

import turtle

def main():
    # stuff
    t = turtle.Turtle()

    # circle
    t.color("red3")
    t.begin_fill()
    t.circle(100)
    t.end_fill()

    # prep for G
    t.penup()
    t.color("white")
    t.left(90)
    t.forward(180)
    t.left(90)
    t.pendown()
    t.begin_fill()
    
    # letter G
    t.circle(80,270)
    t.left(90)
    t.forward(50)
    t.left(90)
    t.forward(10)
    t.left(90)
    t.forward(40)
    t.left(90)
    t.forward(10)
    t.circle(70,-270)
    t.right(90)
    t.forward(10)
    t.end_fill()

    # prep for L
    t.penup()
    t.left(180)
    t.forward(40)
    t.pendown()
    t.begin_fill()

    # letter L
    t.forward(70)
    t.left(90)
    t.forward(30)
    t.left(90)
    t.forward(10)
    t.left(90)
    t.forward(20)
    t.right(90)
    t.forward(60)
    t.left(90)
    t.forward(10)
    t.end_fill()
    
    # prep for dot
    t.penup()
    t.forward(30)
    t.pendown()
    t.begin_fill()

    # dot / eye
    t.circle(10)
    t.end_fill()

    # prep for text
    t.penup()
    t.left(90)
    t.forward(100)
    t.left(90)
    t.forward(130)
    t.pencolor("black")

    # text and finish up
    t.write("LG", font=("Helvetica", 100, "bold"))
    t.hideturtle()

main()
turtle.done()
