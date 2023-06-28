from turtle import Screen
import time
from snake import Snake

screen = Screen()
screen.title('Snake')
screen.bgcolor('black')
screen.screensize(600, 600)
screen.tracer(0)

snake = Snake()

while True:
    time.sleep(.1)
    snake.update()
    screen.update()

screen.exitonclick()