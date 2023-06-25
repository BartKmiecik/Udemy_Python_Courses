# ###This code will not work in repl.it as there is no access to the colorgram package here.###
# ##We talk about this in the video tutorials##
# import colorgram
#
# rgb_colors = []
# colors = colorgram.extract('image.jpg', 30)
# for color in colors:
#     r = color.rgb.r
#     b = color.rgb.b
#     g = color.rgb.g
#     rgb_colors.append((r, g, b))
#
# print(rgb_colors)
import random
from turtle import Turtle, Screen
color_map = [(202, 164, 110),(149, 75, 50), (222, 201, 136), (53, 93, 123), (170, 154, 41), (138, 31, 20), (134, 163, 184), (197, 92, 73), (47, 121, 86), (73, 43, 35), (145, 178, 149), (14, 98, 70), (232, 176, 165), (160, 142, 158), (54, 45, 50), (101, 75, 77), (183, 205, 171), (36, 60, 74), (19, 86, 89), (82, 148, 129), (147, 17, 19), (27, 68, 102), (12, 70, 64), (107, 127, 153), (176, 192, 208), (168, 99, 102)]

screen = Screen()
screen.colormode(255)
screen.screensize(100, 100)
screen.reset()
screen.setworldcoordinates(-120,-120,120,120)

turtle = Turtle()

def get_random_color():
    return color_map[random.randint(0, len(color_map)-1)]

def paint():
    turtle.pensize(50)
    turtle.pu()
    turtle.goto(-100, -100)
    turtle.speed(1000)
    for height in range(-5, 5):
        for width in range(-5, 5):
            turtle.color(get_random_color())
            turtle.goto(width * 20,height * 20)
            turtle.pd()
            turtle.forward(1)
            turtle.pu()


paint()
screen.exitonclick()