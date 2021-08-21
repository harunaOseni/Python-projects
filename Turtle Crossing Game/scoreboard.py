from turtle import Turtle

FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle): 
    def __init__(self): 
        super().__init__()
        self.penup()
        self.hideturtle()
        self.color("black")
        self.score = 0
        self.setposition(-220, 260) 
        self.write(f"LEVEL: {self.score}", align="center", font=FONT)

    def update_level(self):
        self.clear()
        self.score += 1
        self.setposition(-220, 260)
        self.color("black")
        self.write(f"LEVEL: {self.score}", align="center", font=FONT)
    

    def game_over(self):
        self.setposition(0, 0)
        self.write("GAME OVER", align="center", font=FONT)