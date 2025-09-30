from turtle import Turtle, Screen

kim = Turtle()
screen = Screen()

screen.listen()

def move_forwards():
    kim.forward(10)

screen.onkey(key="space" , fun= move_forwards)


screen.exitonclick()