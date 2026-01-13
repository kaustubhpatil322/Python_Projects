from tkinter import *
import pandas
import random

BACKGROUND_COLOR = "#B1DDC6"
to_learn ={}
try:
    data = pandas.read_csv("data/words_to_learn.csv")
except FileNotFoundError:
    original_data = pandas.read_csv("data/french_words.csv")
    to_learn = original_data.to_dict(orient="records")
else:
    to_learn = data.to_dict(orient="records")  # to transform a normal csv's orientation into dict as per the Columns(as key)


#to_learn =to_dict(data) convert into dict
print(to_learn)
#----------------------------------------Methods-------------------------------------------------------------------

def next_card():
    global current_card , flip_timer
    window.after_cancel(flip_timer)
    current_card = random.choice(to_learn)
    canvas.itemconfig(card_title , text="French" , fill="black")
    canvas.itemconfig(card_word , text = current_card["French"] , fill="black" )
    canvas.itemconfig(card_background , image = card_front_img)

def cross_btn_action():
    flip_timer = window.after(3000, func=flip_card)

def flip_card():
    canvas.itemconfig(card_title , text="English" , fill="white")
    canvas.itemconfig(card_word , text = current_card["English"] , fill="white")
    canvas.itemconfig(card_background , image= card_back_img)

def is_known():
    to_learn.remove(current_card)
    learn_data = pandas.DataFrame(to_learn)
    learn_data.to_csv("data/words_to_learn.csv" , index = False)
    next_card()
#----------------------------------------------------UI Setup------------------------------------------------------
window = Tk()
window.title("Flashy")
window.config(padx = 50 , pady = 50 , bg=BACKGROUND_COLOR)

flip_timer = window.after(3000 , func = flip_card)

canvas = Canvas(width = 800 , height = 526)
card_front_img = PhotoImage(file = "images/card_front.png")
card_back_img = PhotoImage(file = "images/card_back.png")
card_background = canvas.create_image(400 , 263 , image = card_front_img)

card_title = canvas.create_text(400 , 150 ,text = "Title", font=("Ariel" , 40 , "italic"))
card_word = canvas.create_text(400 , 263 ,text = "word", font = ( "Ariel" , 60 , "bold"))
canvas.config(bg=BACKGROUND_COLOR , highlightthickness=0)
canvas.grid(row = 0 , column=0 , columnspan = 2 )

cross_img = PhotoImage(file="images/wrong.png")
btn_cross = Button(image = cross_img , highlightthickness=0 , command = cross_btn_action)
btn_cross.grid(row = 1 , column = 0)

check_img = PhotoImage( file = "images/right.png")
btn_check = Button(image = check_img , highlightthickness= 0 , command= is_known)
btn_check.grid(row = 1  , column = 1)


next_card()
window.mainloop()