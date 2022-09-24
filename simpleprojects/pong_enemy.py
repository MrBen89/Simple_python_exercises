from turtle import Turtle, Screen

MOVE_DISTANCE = 20

class EnemyPaddle(Turtle):
    def __init__(self):
        super().__init__()
        self.create_paddle()

    def create_paddle(self):
        self.shape("square")
        self.color("white")
        self.penup()
        self.goto(550, 0)
        self.resizemode("user")
        self.shapesize(1, 4, 1)


    def match_ball(self, ball):
        if self.ycor() < ball.ycor():
            self.setheading(90)
            self.forward(20)
        elif self.ycor() > ball.ycor():
            self.setheading(270)
            self.forward(20)
