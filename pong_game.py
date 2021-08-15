from turtle import Turtle, Screen, time
from paddle import Paddle
from pong_ball import Ball
from score_board import ScoreBoard

screen = Screen()
screen.title("Pong Game")
screen.bgcolor("black")
screen.setup(width=800, height=600)

screen.tracer(0)

right_paddle = Paddle(0, 350)
left_paddle = Paddle(0, -350)
pong_ball = Ball()
score_board = ScoreBoard()

screen.listen()
screen.onkeypress(right_paddle.move_up, "Up")
screen.onkeypress(right_paddle.move_down, "Down")
screen.onkeypress(left_paddle.move_up, "w")
screen.onkeypress(left_paddle.move_down, "s")


pong_game_is_running = True

while pong_game_is_running:
    screen.update()
    pong_ball.move()
    time.sleep(pong_ball.ball_speed)

    if pong_ball.collision(right_paddle):
        pong_ball.bounce_off_paddle()

    elif pong_ball.collision(left_paddle):
        pong_ball.bounce_off_paddle()

    if pong_ball.detect_out_of_bounds():
        score_board.update_left_score()
        pong_ball.refresh_ball()

    if pong_ball.detect_out_of_bounds() == False:
        score_board.update_right_score() 
        pong_ball.refresh_ball()

    if score_board.right_score == 10 or score_board.left_score == 10:
        score_board.game_over()
        pong_game_is_running = False


screen.exitonclick() 