from turtle import Turtle, Screen
import random

timmy_the_turtle = Turtle()
timmy_the_turtle.shape("turtle")
timmy_the_turtle.color("red", "green")

screen = Screen()

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



def draw_regular_shapes(size, sides):
    for i in range(sides):
        timmy_the_turtle.forward(size)
        timmy_the_turtle.left(360/sides)

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
        timmy_the_turtle.pendown()

def random_walk(length):
    screen.colormode(255)
    timmy_the_turtle.speed(0)
    timmy_the_turtle.pensize(5)
    for step in range(length):
        choice = random.randint(0,4)
        if choice == 1:
            timmy_the_turtle.left(90)
        if choice == 2:
            timmy_the_turtle.left(180)
        if choice == 3:
            timmy_the_turtle.left(270)
        timmy_the_turtle.forward(25)
        timmy_the_turtle.pencolor(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

#random_walk(100)

def draw_circles(number):
    screen.colormode(255)
    timmy_the_turtle.speed(0)
    for i in range(number):
        timmy_the_turtle.circle(100)
        timmy_the_turtle.left(360/number)
        timmy_the_turtle.pencolor(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

draw_circles(50)

#for x in range(3, 20):
    #draw_regular_shapes(100, x)


screen.exitonclick()
