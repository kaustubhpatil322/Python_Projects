from turtle import Turtle , Screen
import random

screen = Screen()
screen.setup(width=500 , height = 400)
user_bet = screen.textinput(title="Make a Bet", prompt="Which turtle will win the race? Enter a color: ")
print(user_bet)


tim = Turtle()
jim  = Turtle()
kim  = Turtle()
sim  = Turtle()
vim = Turtle()

y_val = -100
turtle_team = [tim , jim , kim , sim , vim]
color_arr = ["purple" , "red" , "green" , "brown" , "black"]
i=0
for  player in turtle_team:
    player.shape("turtle")
    player.color(color_arr[i])
    player.goto(x = -250 , y = y_val)
    i += 1
    y_val += 50

def move_forward(turtle_obj):
    step = random.randint(1 , 30)
    turtle_obj.forward(step)


over = False
while not over:
    for player in turtle_team:
        move_forward(player)
        if player.xcor() >= 250:
            if user_bet == player.pencolor():
                print("You Win !!")
            else:
                print("You Lose!!")
            print(f"{player.pencolor()} Turtle wins the race.")
            over = True

screen.exitonclick()