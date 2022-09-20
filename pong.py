from turtle import Screen
import random
import time
from pong_paddle import Paddle
#from pong_enemy import EnemyPaddle
from pong_ball import Ball
from pong_score import Scoreboard

screen = Screen()
screen.setup(width=1200, height=800)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)

game_is_on = True

ball = Ball()
paddle1 = Paddle()
paddle2 = Paddle()
#enemy = EnemyPaddle()
scoreboard = Scoreboard()

paddle1.paddle_loc(-550)
paddle2.paddle_loc(550)

screen.listen()

screen.onkeypress(paddle2.up, "Up")
screen.onkeypress(paddle2.down, "Down")
screen.onkeypress(paddle1.up, "w")
screen.onkeypress(paddle1.down, "s")


while game_is_on:
    screen.update()
    time.sleep(0.001)
    ball.move()
    #enemy.match_ball(ball)
    if ball.distance(paddle1) < 40:
        ball.bounce_paddle()
    if ball.distance(paddle2) < 40:
        print("bounce")
        ball.bounce_paddle()

    if ball.xcor() < paddle1.xcor():
        scoreboard.increase_score(2)
        ball.new_ball()
    if ball.xcor() > paddle2.xcor():
        scoreboard.increase_score(1)
        ball.new_ball()

screen.exitonclick()
