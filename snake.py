from turtle import Turtle, Screen


class Snake():
    def __init__(self):
        self.snake = []
        self.x_position = [-20, -40, -60]
        self.screen = Screen()
        for snake_body in range(3):
            self.snake_body = Turtle(shape="square")
            self.snake_body.color("white")
            self.snake_body.penup()
            self.snake_body.goto(x=self.x_position[snake_body], y=0)
            self.snake_body.shapesize(stretch_len=1)
            self.snake.append(self.snake_body)

    def snake_grow(self):
        for snake_body in range(1):
            self.snake_body = Turtle(shape="square")
            self.snake_body.color("white")
            self.snake_body.penup()
            self.snake_body.goto(x=self.x_position[snake_body], y=0)
            self.snake_body.shapesize(stretch_len=1)
            self.snake.append(self.snake_body)

    def move(self):
        for snake_body in range(len(self.snake) - 1, 0, -1):
            self.snake[snake_body].goto(
                x=self.snake[snake_body - 1].xcor(), y=self.snake[snake_body - 1].ycor())
        self.snake[0].forward(10) 

    def reset(self):
        #clear previous snake 
        for snake_body in self.snake:
            snake_body.hideturtle()
        self.snake = []
        self.x_position = [-20, -40, -60]
        for snake_body in range(3):
            self.snake_body = Turtle(shape="square")
            self.snake_body.color("white")
            self.snake_body.penup()
            self.snake_body.goto(x=self.x_position[snake_body], y=0)
            self.snake_body.shapesize(stretch_len=1)
            self.snake.append(self.snake_body)
    
    def left(self):
        if self.snake[0].heading() != 0:
            self.snake[0].setheading(180)
    
    def right(self):
        if self.snake[0].heading() != 180:
            self.snake[0].setheading(0)

    def up(self):
        if self.snake[0].heading() != 270:
            self.snake[0].setheading(90)
    
    def down(self):
        if self.snake[0].heading() != 90:
            self.snake[0].setheading(270) 