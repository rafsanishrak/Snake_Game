from turtle import Turtle
from snake import Snake
import random


class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_wid=0.6, stretch_len=0.6)
        self.color("Yellow")
        self.speed("fastest")
        self.move()

    def move(self):
        x_axis = random.randint(-330, 330)
        y_axis = random.randint(-230, 200)
        self.goto(x_axis, y_axis)


