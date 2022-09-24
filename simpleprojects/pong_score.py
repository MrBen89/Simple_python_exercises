from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score1 = 0
        self.score2 = 0
        self.hideturtle()
        self.penup()
        self.color("white")
        self.speed("fastest")
        self.goto(0, 360)
        self.write(f"{self.score1}  :  {self.score2}", False, "center", ("Arial", 24, "normal"))

    def increase_score(self, player):
        if player == 1:
            self.score1 += 1
        elif player == 2:
            self.score2 += 1
        self.clear()
        self.write(f"{self.score1}  :  {self.score2}", False, "center", ("Arial", 24, "normal"))

    def game_over(self):
        self.goto(0, 0)
        self.write("Game over!", False, "center", ("Arial", 64, "normal"))
