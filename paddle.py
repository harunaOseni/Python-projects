from turtle import Turtle
class Paddle(Turtle):
    def __init__(self, position_x, position_y): 
        super().__init__()
        self.shape("square")
        self.color("white")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.penup()
        self.goto(y=position_x, x=position_y)


    def move_up(self):
        y = self.ycor()
        y += 20
        self.sety(y)
    
    def move_down(self):
        y = self.ycor()
        y -= 20
        self.sety(y)

    


