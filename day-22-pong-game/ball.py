from turtle import Turtle
import random
UP_WALL= 290
DOWN_WALL = -290


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.setheading(45)
        self.shape("circle")
        self.color("turquoise")
        self.penup()
        self.speed("fast")
        self.shapesize(stretch_len = 0.5 , stretch_wid = 0.5)
        self.move_x = 10
        self.move_y = 10
        self.move_speed  = 0.1

    def move(self):
        new_x = self.xcor() + self.move_x
        new_y = self.ycor() + self.move_y
        self.goto(new_x , new_y)

    def detect_collision_with_wall(self):
        if self.ycor() >= UP_WALL or self.ycor() <= DOWN_WALL:
            return True
        return False

    def bounce_x(self):
        self.move_x *= -1
        self.move_speed *= 0.9

    def bounce_y(self):
        self.move_y *= -1

    def reset_position(self):
        self.goto(x=0 , y=0)
        self.move_speed = 0.1



