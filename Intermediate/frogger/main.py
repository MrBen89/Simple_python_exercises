import time
import random
from turtle import Screen
from player import Player
from car_manager import CarManager, Car
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
screen.listen()

player = Player()
car_manager = CarManager()
scoreboard = Scoreboard()

screen.onkeypress(player.move, "Up")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    car_manager.move_cars()
    car_manager.create_car()
    if player.is_finished():
        scoreboard.level_up()
        player.reset_player()
        car_manager.increase_speed()
    if car_manager.collision(player.xcor(), player.ycor()):
        scoreboard.game_over()
        game_is_on = False

screen.exitonclick()
