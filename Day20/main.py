from turtle import Screen
import time
from snake import Snake
from scoreboard import Scoreboard
from food import Food

screen = Screen()
screen.screensize(600, 600)
screen.title('Snake')
screen.bgcolor('black')
screen.tracer(0)
snake = Snake()
scoreboard = Scoreboard()
food = Food()
screen.onkey(snake.move_up, 'w')
screen.onkey(snake.move_down, 's')
screen.onkey(snake.move_right, 'd')
screen.onkey(snake.move_left, 'a')
screen.listen()

game_on = True

while game_on:
    time.sleep(.1)
    snake.update()
    screen.update()

    if snake.head.distance(food) < 15:
        food.spawn_food()
        scoreboard.update_score()
        snake.add_body()
    if snake.head.pos()[0] > 290 or snake.head.pos()[0] < -290 or snake.head.pos()[1] > 290 or snake.head.pos()[1] < -290:
        scoreboard.game_over()
        game_on = False
    for body in snake.turtles[1:]:
        if snake.head.distance(body) < 20:
            scoreboard.game_over()
            game_on = False


screen.exitonclick()