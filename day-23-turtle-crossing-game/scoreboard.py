from turtle import Turtle

FONT = ("Courier" , 24 , "normal")
ALIGN = "left"

class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.level = 1

        self.hideturtle()
        self.penup()
        self.goto(x=-240 , y=240)
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f"Level: {self.level}" , align=ALIGN , font=FONT)

    def increase_level(self):
        self.level += 1
        self.update_scoreboard()

    def game_over(self):
        self.goto(x=0,y=0)
        self.write(f"GAME OVER" , align="center" , font=FONT)

