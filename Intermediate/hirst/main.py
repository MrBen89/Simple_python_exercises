import colorgram
from turtle import Turtle, Screen
import random

timmy_the_turtle = Turtle()
timmy_the_turtle.hideturtle()

screen = Screen()

colors = colorgram.extract("hirst.jpg", 25)

color_list = []

for color in colors:
    color_list.append((color.rgb.r, color.rgb.g, color.rgb.b))

def dot_painting():
    screen.colormode(255)
    timmy_the_turtle.speed(0)
    timmy_the_turtle.penup()
    for y in range(10):
        for x in range(10):
            timmy_the_turtle.dot(20, random.choice(color_list))
            timmy_the_turtle.forward(40)
        timmy_the_turtle.left(180)
        timmy_the_turtle.forward(400)
        timmy_the_turtle.right(90)
        timmy_the_turtle.forward(40)
        timmy_the_turtle.right(90)

dot_painting()
screen.exitonclick()
