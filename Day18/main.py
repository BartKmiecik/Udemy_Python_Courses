from turtle import Screen, Turtle
import random
tim = Turtle()
tim.shape("turtle")
tim.color("red")
screen = Screen()
screen.colormode(255)

def get_random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return r, g, b

def draw_shape(corners: int):
    color = get_random_color()
    screen.colormode(255)
    tim.pencolor((color[0], color[1], color[2]))
    tim.pd()
    for i in range(corners):
        tim.forward(100)
        tim.right(360 / corners)

def random_walk(steps: int):
    size = 4
    speed = 4
    for i in range(steps):
        tim.pensize(size)
        tim.speed(speed)
        color = get_random_color()
        tim.pencolor((color[0], color[1], color[2]))
        rand = random.randint(0, 4)
        tim.forward(100)
        tim.right(90 * rand)
        size += 1
        speed += 0.3

def spirograph(steps: int, radius: float):
    for i in range(steps):
        tim.pensize(3)
        tim.speed(30)
        color = get_random_color()
        tim.pencolor((color[0], color[1], color[2]))
        tim.circle(radius)
        tim.right(360 / steps)

spirograph(60, 100)

screen.exitonclick()