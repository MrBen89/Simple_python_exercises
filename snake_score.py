from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        with open("snake_score.txt") as file:
            self.high_score = int(file.read())
        self.hideturtle()
        self.penup()
        self.color("white")
        self.speed("fastest")
        self.goto(0, 260)
        self.write(f"Score: {self.score} High Score: {self.high_score}", False, "center", ("Arial", 24, "normal"))

    def increase_score(self):
        self.score += 1
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.score} High Score: {self.high_score}", False, "center", ("Arial", 24, "normal"))


    def game_over(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("snake_score.txt", mode="w") as file:
                file.write(str(self.high_score))
        self.score =0
        self.update_scoreboard()
