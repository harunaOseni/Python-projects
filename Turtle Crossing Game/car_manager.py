from turtle import Turtle
import random
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager:
    def __init__(self):
        self.cars = []
        self.car_speed = 0.1

    def create_cars(self):
        random_chance = random.randint(1, 6) # 1 in 6 chance of a car being created
        if random_chance == 1:
            new_car = Turtle()
            new_car.shape("square")
            new_car.shapesize(stretch_wid=1, stretch_len=2)
            new_car.color(random.choice(COLORS))
            new_car.penup()
            new_car.goto(x=300, y=random.randint(-250, 250))
            new_car.backward(STARTING_MOVE_DISTANCE)
            self.cars.append(new_car)

    def move_cars(self):
        for car in self.cars:
            car.setheading(180)
            car.forward(MOVE_INCREMENT)
