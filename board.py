from turtle import Turtle, Screen

class Board:
    def __init__(self):
        self.score_board = Turtle() 
        self.score = 0
        self.score_board.color("white") 
        self.score_board.fillcolor('white') 
        self.score_board.penup()
        self.score_board.goto(0, 275)
        self.score_board.write(arg=f"Score: {self.score}", align="center", font=("Arial", 16, "bold"))
        self.score_board.hideturtle() 

    def update_score(self):
        self.score += 1
        self.score_board.clear()
        self.score_board.color("white")
        self.score_board.fillcolor('white')
        self.score_board.write(arg=f"Score: {self.score}", align="center", font=("Arial", 16, "bold"))

    def game_over(self):
        #goto the middle of the screen
        self.score_board.goto(0, 0)
        self.score_board.write(arg="Game Over", align="center", font=("Arial", 20, "bold"))



# score = Board()
# print (score.score)
# score.update_score()
# print (score.score)