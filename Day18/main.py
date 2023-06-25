from turtle import Screen, Turtle
import random
tim = Turtle()
tim.shape("turtle")
tim.color("red")

screen = Screen()

def draw_shape(corners: int):
    r = random.randint(0, 256)
    g = random.randint(0, 256)
    b = random.randint(0, 256)
    screen.colormode(255)
    tim.pencolor((r, g, b))
    tim.pd()
    for i in range(corners):
        tim.forward(100)
        tim.right(360 / corners)

for i in range(3, 11):
    draw_shape(i)

screen.exitonclick()