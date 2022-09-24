from turtle import Turtle, Screen
import random

timmy_the_turtle = Turtle()

screen = Screen()

def move_forwards():
    timmy_the_turtle.forward(10)

def turn_left():
    timmy_the_turtle.left(15)

def turn_right():
    timmy_the_turtle.right(15)

def clear_screen():
    timmy_the_turtle.reset()


screen.listen()
screen.onkeypress(move_forwards, "space")
screen.onkeypress(turn_left, "Left")
screen.onkeypress(turn_right, "Right")
screen.onkeypress(clear_screen, "c")







screen.exitonclick()
