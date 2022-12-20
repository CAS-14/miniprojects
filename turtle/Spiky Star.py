import turtle

joe = turtle.Turtle()

joe.speed(1)

num = 1

while True:
    joe.fd(num)
    joe.lt(num)
    num += 1

turtle.done()

# Change the fd (line 10) amt to a constant for size and mess with num add
#   (line 12) to get different patterns

# Change the lt (line 11) amt to a constant for spiraly stuff
