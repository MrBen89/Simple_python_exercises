from turtle import Turtle, Screen

MOVE_DISTANCE = 20

class Paddle(Turtle):
    def __init__(self):
        super().__init__()
        self.create_paddle()

    def create_paddle(self):
        self.shape("square")
        self.color("white")
        self.speed("fastest")
        self.penup()
        self.resizemode("user")
        self.setheading(90)
        self.shapesize(1, 4, 8)

    def up(self):
        self.setheading(90)
        self.forward(20)

    def down(self):
        self.setheading(270)
        self.forward(20)

    def paddle_loc(self, x):
        self.goto(x, 0)
