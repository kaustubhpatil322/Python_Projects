from turtle import Turtle , Screen
from random_walk import random_color
import turtle
turtle.colormode(255)

tam = Turtle()
screen = Screen()
tam.speed("fastest")


for _ in range(100):
    tam.circle(100)
    current_heading = tam.heading()
    tam.setheading(current_heading + 5)
    tam.color(random_color())
screen.exitonclick()

