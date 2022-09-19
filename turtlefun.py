from turtle import Turtle, Screen

timmy_the_turtle = Turtle()
timmy_the_turtle.shape("turtle")
timmy_the_turtle.color("red", "green")

def draw_square(size):
    for i in range(4):
        timmy_the_turtle.forward(size)
        timmy_the_turtle.left(90)
def draw_triangle(size):
    for i in range(3):
        timmy_the_turtle.forward(size)
        timmy_the_turtle.left(120)
def draw_pentagon(size):
    for i in range(5):
        timmy_the_turtle.forward(size)
        timmy_the_turtle.left(72)
def draw_hexagon(size):
    for i in range(6):
        timmy_the_turtle.forward(size)
        timmy_the_turtle.left(60)

def dashed_line(length):
    pendown = True
    drawn = 0
    while length-drawn >= 10:
        if pendown:
            timmy_the_turtle.forward(10)
            drawn += 10
            timmy_the_turtle.penup()
            pendown = False
        else:
            timmy_the_turtle.forward(10)
            drawn += 10
            timmy_the_turtle.pendown()
            pendown = True
    if pendown:
        timmy_the_turtle.pendown()
        timmy_the_turtle.forward(length-drawn)
    else:
        timmy_the_turtle.penup()
        timmy_the_turtle.forward(length-drawn)


dashed_line(55)

screen = Screen()
screen.exitonclick()
