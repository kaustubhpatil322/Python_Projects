from turtle import Turtle
FONT = ("Courier" , 70 , "normal")
ALIGN = "center"
class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.color("white")
        self.hideturtle()
        self.goto(x=0 , y=270)
        self.l_score = 0
        self.r_score = 0
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.goto(x= -100 ,y=200)
        self.write(self.l_score, align=ALIGN, font=FONT)
        self.goto(x= 100 , y=200)
        self.write(self.r_score, align=ALIGN, font=FONT)

    def l_increase_score(self):
        self.l_score += 1
        self.update_scoreboard()
    def r_increase_score(self):
        self.r_score += 1
        self.update_scoreboard()
        return False

    def display_winner(self):
        self.goto(x=0,y=0)
        self.write(f"{"Player 1" if self.l_score >self.r_score else "Player 2" } Wins!!", align = ALIGN , font = FONT)



