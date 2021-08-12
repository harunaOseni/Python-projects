# Instances, state and higher order functions

from turtle import Turtle, Screen

my_turtle = Turtle()
my_screen = Screen()


def move_forward():
    my_turtle.forward(10)


def clockwise():
    my_turtle.right(20)


def move_backward():
    my_turtle.backward(10)


def counter_clockwise():
    my_turtle.left(20)


def clear_drawing():
    my_turtle.clear()
    my_turtle.penup()
    my_turtle.home()
    my_turtle.pendown()


my_screen.onkey(move_forward, "w")
my_screen.onkey(counter_clockwise, "a")
my_screen.onkey(move_backward, "s")
my_screen.onkey(clockwise, "d")
my_screen.onkey(clear_drawing, "c") 


my_screen.listen()
my_screen.mainloop() 