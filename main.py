from turtle import Turtle, Screen, time
from snake import Snake
from food import Food
from board import Board

screen = Screen()
screen.setup(600, 600)
screen.bgcolor("black")
screen.title("Snake in the monkey shadow")
screen.tracer(0)

snake = Snake()
food = Food()
score_board = Board() 


# snake game controls
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

    #code to detect collision between snake and food
    if snake.snake[0].distance(food) < 15:
        food.move_food() # move food to a random position
        score_board.update_score()
        snake.snake_grow()

    #code to detect collision between walls 
    if snake.snake[0].xcor() > 285 or snake.snake[0].xcor() < -285 or snake.snake[0].ycor() > 285 or snake.snake[0].ycor() < -285:
        game_is_running = False
        score_board.game_over()

    #code to detect collision between snake and itself
    for i in range(1, len(snake.snake)):
        if snake.snake[0].distance(snake.snake[i]) < 5:
            game_is_running = False
    


screen.exitonclick() 