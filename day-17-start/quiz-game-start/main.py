from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank=[]
for  que in question_data:
    question_bank.append(Question(que["question"] , que["correct_answer"]))

quiz= QuizBrain(question_bank)

while quiz.still_has_questions():
    quiz.next_question()
quiz.display_final_score()