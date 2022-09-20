from turtle import Screen
import random
import time
from snake_snake import Snake
from snake_food import Food
from snake_score import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake")
screen.tracer(0)

game_is_on = True

snake = Snake()
food = Food()
scoreboard = Scoreboard()

screen.listen()

screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    #Food collision
    if snake.segments[0].distance(food) < 20:
        food.refresh()
        scoreboard.increase_score()
        snake.extend()

    #Wall collision
    if snake.segments[0].xcor() > 280 or snake.segments[0].xcor() < -280 or snake.segments[0].ycor() > 280 or snake.segments[0].ycor() < -280:
        scoreboard.game_over()
        game_is_on = False

    #Tail collision
    for segment in snake.segments:
        if segment != snake.segments[0]:
            if snake.segments[0].distance(segment) < 10:
                scoreboard.game_over()
                game_is_on = False

screen.exitonclick()
