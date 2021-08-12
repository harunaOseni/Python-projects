from turtle import Turtle, Screen
import random
from tkinter import *
from tkinter import messagebox

root = Tk()
screen = Screen()
screen.setup(width=500, height=400)
users_bet = screen.textinput("The Turtle Race", "Enter a turtle color\
 to place a bet: ")
colors = ["red", "orange",  "yellow", "green", "blue", "purple"]
y = [70, 40, 10, -20, -50, -80]

turtle_racers = []


def random_distance():
    """returns random distances from 1-10"""
    random_distance = random.randint(0, 10)
    return random_distance


def is_winner(user_bet, answer):
    """returns True if the user wins the bet"""
    if user_bet == answer:
        return True
    else:
        return False


for turtle_index in range(6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(colors[turtle_index])
    new_turtle.penup()
    new_turtle.goto(x=-230, y=y[turtle_index])
    turtle_racers.append(new_turtle)

is_race_on = False

if users_bet:
    is_race_on = True

while is_race_on:
    for turtle in turtle_racers:
        if turtle.xcor() > 232:
            is_race_on = False
            if is_winner(users_bet, turtle.pencolor()):
                messagebox.showinfo("Result", "You win what a bet")
            else:
                messagebox.showinfo(
                    "show info", f"you lose the winner was the {turtle.pencolor()} turtle")

        turtle.forward(random_distance())


screen.mainloop()