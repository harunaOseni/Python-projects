# Turtle crossing game
from turtle import Screen, time
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
screen.bgcolor("white")


player = Player()
car_manager = CarManager() 
score_board = Scoreboard()

screen.listen() 
screen.onkey(player.move_up, "Up")


game_is_on = True
while game_is_on:
    time.sleep(car_manager.car_speed)
    screen.update()

    car_manager.create_cars()
    car_manager.move_cars()

    if player.ycor() >= 280:
        score_board.update_level()
        car_manager.car_speed *= 0.9
        player.refresh()
    
    for car in car_manager.cars:
        if player.distance(car) < 20:
            game_is_on = False
            score_board.game_over()


screen.mainloop()