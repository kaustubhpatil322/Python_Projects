from turtle import Turtle, Screen
import turtle as t
import random

def random_color():
    r = random.randint(0 , 255)
    g = random.randint(0 , 255)
    b = random.randint(0 , 255)
    color = (r,g,b)
    return color

if __name__ == "__main__":
    tom = Turtle()
    t.colormode(255)

    screen = Screen()
    tom.speed("fastest")
    tom.pensize(10)

    directions = [0, 90, 180, 270]

    for _ in range(50):
        tom.color(random_color())
        tom.forward(20)
        tom.setheading(random.choice(directions))

    screen.exitonclick()


