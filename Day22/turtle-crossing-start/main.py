import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
player = Player()
screen.listen()
screen.onkey(player.move_forward, 'w')
screen.onkeypress(player.move_forward, 'w')
car_manager = CarManager()
scoreboard = Scoreboard()

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    car_manager.update()
    screen.update()

    for car in car_manager.cars:
        if car.distance(player) < 30:
            game_is_on = False
            scoreboard.game_over()

    if player.pos()[1] > 280:
        scoreboard.update_level()
        car_manager.increase_level()
        player.reset()


screen.exitonclick()
