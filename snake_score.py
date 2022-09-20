from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.hideturtle()
        self.penup()
        self.color("white")
        self.speed("fastest")
        self.goto(0, 260)
        self.write(f"Score: {self.score}", False, "center", ("Arial", 24, "normal"))

    def increase_score(self):
        self.score += 1
        self.clear()
        self.write(f"Score: {self.score}", False, "center", ("Arial", 24, "normal"))

    def game_over(self):
        self.goto(0, 0)
        self.write("Game over!", False, "center", ("Arial", 64, "normal"))
