import colorgram
import turtle as t
"""t - Turtle Module"""
import random
tim = t.Turtle()
screen = t.Screen()

t.colormode(255)


color_list = [(249, 228, 17),
 (213, 13, 9),
 (198, 12, 35),
 (231, 228, 5),
 (197, 69, 20),
 (33, 90, 188),
 (43, 212, 71),
 (234, 148, 40),
 (33, 30, 152),
 (16, 22, 55),
 (66, 9, 49),
 (244, 39, 149),
 (65, 202, 229),
 (14, 205, 222),
 (63, 21, 10),
 (224, 19, 111),
 (229, 165, 8),
 (15, 154, 22),
 (245, 58, 16),
 (98, 75, 9),
 (248, 11, 9),
 (222, 140, 203),
 (68, 240, 161),
 (10, 97, 62),
 (5, 38, 33),
 (68, 219, 155)]
tim.penup()

tim.setheading(225)
tim.forward(300)
tim.setheading(0)

for _ in range(10):
    for _ in range(10):
        tim.dot(20, random.choice(color_list))
        tim.forward(50)
    tim.setheading(90)
    tim.forward(50)
    tim.setheading(180)
    tim.forward(500)
    tim.setheading(0)


screen.exitonclick()


