from turtle import Turtle, Screen
import time
from snake import Snake
from food import Food
from scoreboard import Scoreboard


screen = Screen()
screen.bgcolor("Black")
screen.tracer(0)
screen.setup(width=700, height=500)
screen.title("Snake Game")
segments = []


snake = Snake()
food = Food()
score = Scoreboard()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

game_on = True
while game_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    if snake.head.distance(food) < 15:
        food.move()
        snake.extend()
        score.inc_score()

    if snake.head.xcor() > 350 or snake.head.xcor() < -350 or snake.head.ycor() > 240 or snake.head.ycor() < -250:
        game_on = False
        score.game_over()

    for segment in snake.segments:

        if segment == snake.head:
            pass

        elif snake.head.distance(segment) < 10:
            game_on = False
            score.game_over()


















screen.exitonclick()