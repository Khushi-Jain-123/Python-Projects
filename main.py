from turtle import Turtle, Screen
import time
from snake import Snake
from food import Food
from score import Score


screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)
game_is_on = True
screen.listen()
snake = Snake()
rand_food = Food()
score = Score()
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")

while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    if snake.head.distance(rand_food) < 15:
        rand_food.refresh()
        score.increase_score()
        snake.create_segment()

    if snake.head.xcor() > 290 or snake.head.xcor() < -290 or snake.head.ycor() > 290 or snake.head.ycor() < -290:
        score.reset()
        snake.reset()

    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 5:
            score.reset()
            snake.reset()


screen.exitonclick()
