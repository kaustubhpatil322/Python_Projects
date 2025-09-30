from turtle import Turtle
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

class Snake:
    def __init__(self):
        self.segment_arr = []
        self.create_segment()
        self.head = self.segment_arr[0]

    def move(self):
        last_index = len(self.segment_arr) -1
        for i in range(last_index , 0 , -1):
            self.segment_arr[i].hideturtle()
            self.segment_arr[i].goto(self.segment_arr[i-1].xcor(), self.segment_arr[i-1].ycor())
            self.segment_arr[i].showturtle()
        self.head.forward(MOVE_DISTANCE)

        self.head.hideturtle()

        if self.head.xcor() >= 290:
            self.head.goto(-300, self.head.ycor())
        elif self.head.ycor() >= 290:
            self.head.goto(self.head.xcor() , -290)
        elif self.head.xcor() <= -290:
            self.head.goto(290 , self.head.ycor())
        elif self.head.ycor() <= -290:
            self.head.goto(self.head.xcor() , 290)
        self.head.showturtle()


    def create_segment(self):
        segment = Turtle()
        segment.penup()
        segment.speed("fast")
        segment.color("white")
        segment.shape("square")
        segment.hideturtle()
        if len(self.segment_arr) > 1:
            last_segment = self.segment_arr[-1]
            if last_segment.heading() == UP:
                segment.goto(last_segment.xcor() , last_segment.ycor() - MOVE_DISTANCE)
            elif last_segment.heading() == DOWN:
                segment.goto(last_segment.xcor() , last_segment.ycor() + MOVE_DISTANCE)
            elif last_segment.heading() == LEFT:
                segment.goto(last_segment.xcor() + MOVE_DISTANCE , last_segment.ycor())
            elif last_segment.heading() == RIGHT:
                segment.goto(last_segment.xcor() - 20 , last_segment.ycor())
        segment.showturtle()
        self.segment_arr.append(segment)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)


