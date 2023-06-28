from turtle import Screen
import time
from snake import Snake

screen = Screen()
screen.title('Snake')
screen.bgcolor('black')
screen.screensize(600, 600)
screen.tracer(0)
snake = Snake()


screen.onkey(snake.move_up, 'w')
screen.onkey(snake.move_down, 's')
screen.onkey(snake.move_right, 'd')
screen.onkey(snake.move_left, 'a')
screen.listen()

while True:
    time.sleep(.1)
    snake.update()
    screen.update()

screen.exitonclick()