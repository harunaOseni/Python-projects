# Turtle Graphics, Tuples and importing modules
import turtle

tim_the_turtle = turtle.Turtle()
tim_the_turtle.color("green")
tim_the_turtle.shape("turtle")


# for i in range(4):
#     tim_the_turtle.forward(100)
#     tim_the_turtle.left(90)

# for i in range(11):
#     tim_the_turtle.forward(5)
#     tim_the_turtle.penup()
#     tim_the_turtle.forward(5)
#     tim_the_turtle.pendown()

# side = 3
# color_count = 0
#a list of 15 images 
colors = ["red", "orange", "yellow", "green", "blue", "indigo", "violet", "purple", "pink", "brown", "grey", "black"]


# def make_shape():
#     global side
#     global color_count
#     while side < 11:
#         for _ in range(side):
#             tim_the_turtle.forward(100)
#             tim_the_turtle.right(360/side)
#         tim_the_turtle.color(colors[color_count])
#         side += 1
#         color_count += 1

import random
import colorgram


tim_the_turtle.speed("fastest")
tim_the_turtle.pensize(1)
turtle.colormode(255)

# def random_numbers():
#     degrees = [0, 90, 180, 270]
#     return random.choice(degrees) 

# def random_colors(): 
#     r = random.randint(0, 255)
#     g = random.randint(0, 255)
#     b = random.randint(0, 255)
#     return (r, g, b)

# def random_walk(): 
#     
#     while distance < 150:
#         tim_the_turtle.color(random_colors())
#         tim_the_turtle.forward(30)
#         tim_the_turtle.setheading(random_numbers())
#         distance += 1

#hide the turtle
# tim_the_turtle.hideturtle()

# distance = 0
# while distance < 40:
#     tim_the_turtle.color(random_colors())
#     tim_the_turtle.circle(100)
#     tim_the_turtle.left(10)
#     distance += 1

# Extract 6 colors from an image.
# colors = colorgram.extract('damien_art.jfif', 30)
# first_color = colors[0]
# rgb_of_first_color = first_color.rgb
# print(rgb_of_first_color.r)

hirst_colors = [(237, 224, 80), (205, 4, 73), (236, 50, 130), (198, 164, 8), (111, 179, 218), (204, 75, 12), (219, 161, 103), (234, 224, 4), (11, 23, 63), (29, 189, 111), (22, 107, 174), (16, 28, 177), (216, 134, 179), (8, 186, 216), (229, 167, 200), (210, 25, 148), (122, 190, 160), (7, 49, 26), (34, 136, 72), (63, 20, 7), (126, 219, 234), (190, 14, 4), (109, 87, 215), (140, 217, 202), (238, 64, 34), (71, 10, 28)]

# for color in colors:
#     rgb_tuple = ()
#     rgb = color.rgb
#     rgb_red = rgb.r
#     rgb_green = rgb.g
#     rgb_blue = rgb.b
#     rgb_tuple = (rgb_red, rgb_green, rgb_blue)
#     hirst_colors.append(rgb_tuple)


x = -120
y = -100

#function to create generate random hirst colors
def random_hirst_colors():
    global hirst_colors
    random_color = random.choice(hirst_colors)
    return random_color


def hirst_painting():
    global x
    global y
    for _ in range(10):
        tim_the_turtle.penup()
        tim_the_turtle.goto(x, y)
        y += 50
        for _ in range(10):
            tim_the_turtle.dot(15, random_hirst_colors())
            tim_the_turtle.penup()
            tim_the_turtle.forward(40)
            tim_the_turtle.pendown()

hirst_painting()







turtle_screen = turtle.Screen()
turtle_screen.exitonclick() 
