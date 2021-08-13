from turtle import Turtle, Screen, time
from snake import Snake

screen = Screen()
screen.setup(600, 600)
screen.bgcolor("black")
screen.title("Snake in the monkey shadow")
screen.tracer(0)

snake = Snake()


#snake game controls
screen.listen()
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")


game_is_running = True

while game_is_running:
    snake.move() 
    screen.update()
    time.sleep(0.1)  



screen.exitonclick() 