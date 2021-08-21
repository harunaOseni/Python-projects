from turtle import Turtle, Screen

class Board:
    def __init__(self):
        self.score_board = Turtle() 
        self.score = 0
        with open("high_score.txt", "r") as file:
            self.high_score = int(file.read())
        self.score_board.color("white") 
        self.score_board.fillcolor('white') 
        self.score_board.penup()
        self.score_board.goto(0, 275)
        self.score_board.write(arg=f"Score: {self.score} High_Score: {self.high_score}", align="center", font=("Arial", 16, "bold"))
        self.score_board.hideturtle() 

    def update_score(self):
        self.score += 1
        if self.score > self.high_score:
            self.high_score = self.score
        self.score_board.clear()
        self.score_board.color("white")
        self.score_board.fillcolor('white')
        self.score_board.write(arg=f"Score: {self.score} High_Score: {self.high_score}", align="center", font=("Arial", 16, "bold"))

    def reset_score(self):
        if self.score > self.high_score:
            with open("high_score.txt", "w") as file:
                file.write(str(self.score))
            self.high_score = self.score
        self.score = 0
        self.score_board.clear()
        self.score_board.color("white")
        self.score_board.write(arg=f"Score: {self.score} High_Score: {self.high_score}", align="center", font=("Arial", 16, "bold"))




# score = Board()
# print (score.score)
# score.update_score()
# print (score.score)