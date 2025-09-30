from turtle import Turtle , Screen


tim = Turtle()
screen = Screen()
screen.listen()

tim.speed("fast")

def move_forwards():
    tim.forward(20)

def move_backwards():
    tim.backward(20)

def erase():
    tim.clear()
    tim.penup()
    tim.home()
    tim.pendown()

def turn_left():
    new_heading = tim.heading() + 10
    tim.setheading(new_heading)
    tim.forward(20)
def turn_right():
    new_heading = tim.heading() - 10
    tim.setheading(new_heading)
    tim.forward(20)

def move_clockwise():
    tim.circle(radius=150 , extent = 360/10)

screen.onkey(key="w" , fun = move_forwards)
screen.onkey(key ="s" , fun = move_backwards)
screen.onkey(key = "d" , fun = move_clockwise)
screen.onkey(key = "c" , fun = erase)
screen.onkey(key="r" , fun=turn_right)
screen.onkey(key="l" , fun=turn_left)

screen.exitonclick()