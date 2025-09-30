from turtle import  Screen
from snake import Snake
from food import Food
from scoreboard import ScoreBoard

import time as tym

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")

game_is_on = True
snake = Snake()
food = Food()
scoreboard = ScoreBoard()
screen.listen()
screen.onkey(fun=snake.up, key="Up")
screen.onkey(fun=snake.down, key="Down")
screen.onkey(fun=snake.left, key="Left")
screen.onkey(fun=snake.right, key="Right")

while game_is_on:
    screen.update()
    tym.sleep(0.1)
    snake.move()
    if snake.head.distance(food) <= 15:
        if food.eat():
            snake.create_segment()
            food.refresh()
            scoreboard.increase_score()
    #detect collision with body
    for segment in snake.segment_arr[1:]:
        if snake.head.distance(segment) < 10:
            scoreboard.game_over()
            game_is_on = False


screen.exitonclick()
