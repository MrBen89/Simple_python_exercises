from turtle import Turtle

FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.level = 1
        self.hideturtle()
        self.penup()
        self.color("black")
        self.speed("fastest")
        self.goto(-200, 250)
        self.write(f"Level: {self.level}", False, "center", (FONT))

    def level_up(self):
        self.level += 1
        self.clear()
        self.write(f"Level: {self.level}", False, "center", (FONT))
    
    def game_over(self):
        self.goto(0, 0)
        self.write("Game over!", False, "center", ("Arial", 64, "normal"))
