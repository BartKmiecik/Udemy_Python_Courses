from turtle import Turtle, Screen
from player import Player
from ball import Ball
import time

screen = Screen()
screen.bgcolor('black')
screen.setup(600, 600)
screen.tracer(0)

player = Player(True)
ai = Player(False)
ball = Ball(player, ai)

screen.listen()
screen.onkeypress(player.move_up, 'w')
screen.onkeypress(player.move_down, 's')

for i in range (-270, 290, 50):
    line = Turtle()
    line.pu()
    line.shape('square')
    line.color('white')
    line.shapesize(1, .2)
    line.goto(0, i)

def move_ai():
    if ball.pos()[0] < 0:
        if ball.pos()[1] > 0:
            ai.move_up()
        else:ai.move_down()
    else:
        if ai.pos()[1] < -10:
            ai.move_up()
        elif ai.pos()[1] > 10:
            ai.move_down()

game_on = True
while game_on:
    time.sleep(.03)
    ball.update_ball()
    move_ai()
    screen.update()

screen.exitonclick()