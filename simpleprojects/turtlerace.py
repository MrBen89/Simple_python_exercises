from turtle import Turtle, Screen
import random

red_turtle = Turtle()
blue_turtle = Turtle()
yellow_turtle = Turtle()
green_turtle = Turtle()
purple_turtle = Turtle()

screen = Screen()
screen.setup(width=500, height=400)

all_turtles = []

user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color: ")

def turtle_setup(turtle, color, x, y):
    turtle.shape("turtle")
    turtle.color(color)
    turtle.penup()
    turtle.goto(x,y)
    all_turtles.append(turtle)



turtle_setup(red_turtle, "Red", -220, 170)
turtle_setup(blue_turtle, "blue", -220, 90)
turtle_setup(yellow_turtle, "yellow", -220, 0)
turtle_setup(green_turtle, "green", -220, -90)
turtle_setup(purple_turtle, "purple", -220, -170)

def movement(turtle):
    turtle.forward(random.randint(0,10))

if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in all_turtles:
        movement(turtle)
        if turtle.xcor() > 230:
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color.lower() == user_bet.lower():
                print(f"You've won! the winning color was {winning_color}")
            else:
                print(f"You've lost! the winning color was {winning_color}")

screen.listen()







screen.exitonclick()
