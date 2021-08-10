#computer quiz program

from question_model import *
from data import question_data
from quiz_brain import *

question_bank = []

quiz = QuizBrain(question_bank)

for question in question_data: 
    question_bank.append(Question(question["question"], question["correct_answer"]))


while quiz.more_question(): 
    quiz.next_question()
