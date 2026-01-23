from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"
WHITE = "#FFFFFF"
RED = "#F63049"
GREEN = "#A8DF8E"

class QuizInterface:
    def __init__(self , quiz : QuizBrain):
        self.quiz =quiz
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(padx = 20 , pady = 20 , bg=THEME_COLOR)
        self.score = Label(self.window , text="Score : 0" , bg=THEME_COLOR , font=("Arial",20))
        self.score.config(padx=20, pady=20 , foreground= WHITE)
        self.score.grid(row = 0 , column = 1)
        self.canvas = Canvas(height=250 , width=300 ,bg=WHITE , highlightthickness=0)
        self.question_text = self.canvas.create_text(150 , 120 ,
                                                     text="Question" ,
                                                     fill=THEME_COLOR,
                                                     font=("Arial" , 20 , "italic"),
                                                     width = 280)
        self.canvas.grid(row = 1 , column =0, columnspan=2 , pady=20)
        self.tick_img = PhotoImage(file="images/true.png")

        self.cross_img = PhotoImage(file="images/false.png")

        self.true_button = Button(image=self.tick_img , highlightthickness=0 , command= self.true_pressed)
        self.true_button.grid(row=2 , column=0 , pady=20)
        self.false_button = Button(image= self.cross_img , highlightthickness=0 , command= self.false_pressed)
        self.false_button.grid(row=2 , column=1 , pady=20)
        self.show_que()
        self.prev_state = None
        self.window.mainloop()

    def show_que(self):
        self.canvas.config(bg=WHITE)
        if self.quiz.still_has_questions():
            next_que = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text , text= next_que)
        else:
            self.canvas.itemconfig(self.question_text , text = f"You have completed the quiz. \nFinal Score = {self.quiz.score} ")
            self.score.config(text="")
            self.true_button.config(state = "disabled")
            self.false_button.config(state = "disabled")

    def true_pressed(self):
        is_right = self.quiz.check_answer("True")
        self.update_ui(is_right)

    def false_pressed(self):
        is_right= self.quiz.check_answer("False")
        self.update_ui(is_right)

    def update_ui(self , is_right: bool):

        if is_right:
            self.score.config(text = f"Score : {self.quiz.score}")
            self.canvas.config(bg = GREEN)
        else:
            self.canvas.config(bg= RED)
        self.window.after(1000, self.show_que)#Here () is not needed as the function needs to get called after 1 sec







