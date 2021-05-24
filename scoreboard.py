from turtle import Turtle
from food import Food


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.penup()
        self.color("white")
        self.hideturtle()
        self.update_score()

    def update_score(self):
        self.goto(0, 220)
        self.write(f"Score: {self.score}", align="center", font=("arial", 20, "normal"))

    def game_over(self):
        self.goto(0, 0)
        self.write(f"Game Over !", align="center", font=("arial", 20, "normal"))



    def inc_score(self):
        self.score += 1
        self.clear()
        self.update_score()


