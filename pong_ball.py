from turtle import Turtle
import random

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.color("white")
        self.speed("fast")
        self.direction()

    def direction(self):
        dir = random.randint(0,45)
        if random.randint(0,2):
            dir += 180
        self.setheading(dir)

    def move(self):
        self.forward(5)
        if self.ycor() > 350 or self.ycor() < -350:
            self.setheading(360-self.heading())

    def bounce_paddle(self):
        dir = 180-self.heading()
        if dir < 0:
            dir = 360 + dir
        self.setheading(dir)

    def new_ball(self):
        self.direction()
        self.setposition(0,0)
