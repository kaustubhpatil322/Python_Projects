from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import ScoreBoard
import time as t

screen = Screen()
screen.tracer(0)
screen.setup(width = 800 , height = 600)
screen.bgcolor("black")
screen.title("PONG")

r_paddle = Paddle(position=(350 , 0))
l_paddle = Paddle(position=(-350 , 0))

screen.listen()
screen.onkey(fun= r_paddle.up , key = "Up")
screen.onkey(fun = r_paddle.down , key = "Down")
screen.onkey(fun = l_paddle.up , key = "w")
screen.onkey(fun = l_paddle.down , key="s")

ball = Ball()
scoreboard = ScoreBoard()

game_is_on = True
while game_is_on:
    t.sleep(ball.move_speed)
    ball.move()
    if ball.detect_collision_with_wall():
        ball.bounce_y()
    elif ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() < -320:
        ball.bounce_x()

    if ball.xcor() > 380:
        ball.reset_position()
        scoreboard.l_increase_score()

    if ball.xcor() < -380:
        ball.reset_position()
        scoreboard.r_increase_score()

    if scoreboard.l_score == 5 or scoreboard.r_score==5:
        scoreboard.display_winner()
        game_is_on = False


    screen.update()



screen.exitonclick()