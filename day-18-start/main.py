from turtle import Turtle,Screen
import random

tim = Turtle()
tim.shape("turtle")
tim.color("turquoise")
tim.penup()
tim.sety(tim.ycor() + 450)
tim.pendown()


colors = [
    "red", "green", "blue", "yellow", "orange", "purple", "pink", "brown",
    "black", "white", "gray", "cyan", "magenta", "violet", "indigo", "turquoise",
    "gold", "silver", "navy", "maroon", "lime", "olive", "coral", "tan",
    "wheat", "chocolate", "salmon", "plum", "orchid"
]

for j in range(3,11):
    tim.color(random.choice(colors))
    for i in range(j*5):
        if i % 5 == 0:
            tim.right(360/j)
        tim.forward(20)

screen = Screen()
screen.exitonclick()

import heroes
print(heroes.gen())