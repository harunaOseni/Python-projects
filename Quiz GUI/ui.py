from tkinter import *
from quiz_brain import QuizBrain
THEME_COLOR = "#375362"


class QuizInterface:
    def __init__(self, quiz: QuizBrain):
        self.quiz_brain = QuizBrain(quiz.question_list)
        self.window = Tk()
        self.window.title("Quizly")
        self.window.configure(background=THEME_COLOR, padx=30, pady=30)
        self.score = 0
        self.score_label = Label(bg=THEME_COLOR, fg="white",
                                 text=f"Score: {self.score}", font=("Ariel", 15, "bold"))
        self.score_label.grid(row=0, column=1, pady=20)
        self.canvas = Canvas(self.window, width=300, height=250, bg="white")
        self.canvas.config(width=300)
        self.canvas.grid(row=1, column=0, columnspan=2)
        self.canvas_text = self.canvas.create_text(
            157, 120, text="Amazon acquired Twitch in August 2014 for $970million dollars.", font=("Arial", 20, "italic"), width=300)
        self.true_image = PhotoImage(file="images/true.png")
        self.true_button = Button(
            self.window, text="True", image=self.true_image, command=self.true_answer)
        self.true_button.grid(row=2, column=0, pady=30)
        self.false_image = PhotoImage(file="images/false.png")
        self.false_button = Button(
            self.window, text="True", image=self.false_image, command=self.false_answer)
        self.false_button.grid(row=2, column=1)
        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        if self.quiz_brain.still_has_questions():
            quiz_text = self.quiz_brain.next_question()
            self.canvas.itemconfig(self.canvas_text, text=quiz_text)
        else:
            if self.quiz_brain.score > 5:
                self.canvas.itemconfig(
                    self.canvas_text, text="You have finished the quiz, Hurray!")
            else:
                self.canvas.itemconfig(
                self.canvas_text, text="You have finished the quiz, Better luck next time!")
            self.true_button.config(state=DISABLED)
            self.false_button.config(state=DISABLED)

    def false_answer(self):
        is_right = self.quiz_brain.check_answer("False")
        self.give_feedback(is_right)

    def true_answer(self):
        is_right = self.quiz_brain.check_answer("True")
        self.give_feedback(is_right)

    def give_feedback(self, is_right):
        if is_right:
            self.canvas.configure(bg="green")
            self.window.after(1000, self.change_bg_and_move_to_next_question)
            self.score_label.config(text=f"Score: {self.quiz_brain.score}")
        else:
            self.canvas.configure(bg="red")
            self.window.after(1000, self.change_bg_and_move_to_next_question)

    def change_bg_and_move_to_next_question(self):
        self.canvas.configure(bg="white")
        self.get_next_question()
