from turtle import Turtle


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.dx = 10
        self.dy = 10
        self.shapesize(1)
        self.color("red")
        self.shape("circle")
        self.goto(0, 0)
        self.ball_speed = 0.1

    def move(self):
        self.goto(self.xcor()+self.dx, self.ycor()+self.dy)
        # detect if ball hits the top border
        if self.ycor() > 280:
            self.dy *= -1
        # detect if ball hits the bottom border
        if self.ycor() < -280:
            self.dy *= -1

    def collision(self, other):
        if (self.distance(other) < 50 and self.xcor() > 340) or (self.distance(other) < 50 and self.xcor() < -340):
            return True
        else:
            return False

    def bounce_off_paddle(self):
        self.dx *= -1
        self.ball_speed *= 0.9

    def detect_out_of_bounds(self):
        if self.xcor() > 400: 
            return True
        elif self.xcor() < -400:
            return False

    def refresh_ball(self):
        self.goto(0, 0)
        self.dx *= -1
        self.dy *= -1
        self.shapesize(1)
        self.color("red")
        self.shape("circle")
        self.ball_speed = 0.1