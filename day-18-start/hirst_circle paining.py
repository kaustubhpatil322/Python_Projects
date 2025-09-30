from turtle import Turtle, Screen
import turtle as t
import random
from color_pallete import color_list
jim = Turtle()
screen = Screen()
t.colormode(255)
jim.speed("fast")


jim.penup()
jim.setheading(270)
jim.forward(200)
jim.setheading(0)
for i in range(5 , 0 , -1):
    dots = i*4
    for _ in range(dots):
        jim.dot(10 , random.choice(color_list))
        jim.circle(50*i , 360/dots)
    jim.setheading(90)
    jim.forward(20)
    jim.setheading(0)

screen.exitonclick()