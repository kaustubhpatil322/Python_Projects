import turtle
import pandas


screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

# def get_mouse_cor(x,y):
#     print(x , y)
#
# turtle.onscreenclick(get_mouse_cor)
# turtle.mainloop()
data = pandas.read_csv("50_states.csv")

state_list = data["state"].to_list()

correct =0
writer = turtle.Turtle()
writer.penup()
writer.hideturtle()
guessed_correct = []
while correct != 50:
    answer = screen.textinput(title=f"{correct}/50 Guess the State" , prompt="Can you find the another state")
    guess = answer.title()
    if guess == "Exit":
        missing_state = [ state for state in state_list if state not in guessed_correct]
        df = pandas.DataFrame(missing_state)
        df.to_csv("states_to_learn.csv")
        break
    if guess in state_list:
        correct+=1
        row = data[data["state"] == guess]
        x = int(row.x)
        y = int(row.y)
        writer.goto(x, y)
        writer.write(guess)
        guessed_correct.append(guess)

for state in state_list:
    if state not in guessed_correct:
        row = data[data["state"] == state]
        x = int(row.x)
        y = int(row.y)
        writer.goto(x, y)
        writer.write(state)
        guessed_correct.append(state)

screen.exitonclick()
