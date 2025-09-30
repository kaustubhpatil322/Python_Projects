import turtle as t
from color_pallete import color_list
import random
t.colormode(255)

sim = t.Turtle()
screen  = t.Screen()
sim.speed("fast")
sim.penup()
sim.setheading(180)
sim.forward(100)
sim.setheading(0)

for i in range(1 , 7):
    num_dots = i * 4
    radius = i*50
    for _ in range(num_dots):
        sim.dot(10 , random.choice(color_list))
        sim.circle(radius , 360/num_dots)
    sim.setheading(90)
    sim.forward(radius)
    sim.setheading(270)
    sim.forward(radius+50)
    sim.setheading(0)

screen.exitonclick()
