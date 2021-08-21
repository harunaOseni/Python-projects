from turtle import Turtle, Screen

class ScoreBoard(Turtle): 
    def __init__(self): 
        super().__init__()
        self.color("white")
        self.penup()
        self.speed(0)
        self.setposition(-100, 245) 
        self.left_score = 0
        self.right_score = 0
        self.write(self.left_score, align="center", font=("Courier", 40, "normal"))
        self.setposition(100, 245)
        self.write(self.right_score, align="center", font=("Courier", 40, "normal"))
        #hide the turtle
        self.hideturtle()

    def update_left_score(self):
        self.clear()
        self.left_score += 1
        self.setposition(100, 245) 
        self.write(self.right_score, align="center", font=("Courier", 40, "normal"))
        self.setposition(-100, 245)
        self.write(self.left_score, align="center", font=("Courier", 40, "normal"))

    def update_right_score(self):
        self.clear()
        self.right_score += 1
        self.setposition(100, 245) 
        self.write(self.right_score, align="center", font=("Courier", 40, "normal"))
        self.setposition(-100, 245)
        self.write(self.left_score, align="center", font=("Courier", 40, "normal"))

    def game_over(self):
        self.clear()
        if self.left_score > self.right_score:
            self.write("Left Player Wins!", align="center", font=("Courier", 40, "normal"))
        elif self.right_score > self.left_score:
            self.write("Right Player Wins!", align="center", font=("Courier", 40, "normal"))
        self.hideturtle()