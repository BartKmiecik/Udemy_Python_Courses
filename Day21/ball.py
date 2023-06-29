from turtle import Turtle
import random
import math
from player import Player
class Ball(Turtle):

    def __init__(self, player1: Player, player2: Player):
        super().__init__()
        self.pu()
        self.color('white')
        self.shape('circle')
        self.shapesize(.7, .7)
        self.reset()
        self.player1 = player1
        self.player2 = player2

    def update_ball(self):
        self.check_players()
        self.check_bound()
        self.forward(10)

    def reset(self) -> None:
        initial_rot = random.randint(30, 160)
        x = (-1)**random.randrange(2)
        self.goto(0,0)
        self.setheading(initial_rot * x)


    def check_bound(self):
        if self.pos()[1] >= 280 or self.pos()[1] <= -280:
            self.setheading(0 - self.heading())
        if self.pos()[0] >= 300:
            self.player2.get_Point()
            self.reset()
        elif self.pos()[0] <= -300:
            self.player1.get_Point()
            self.reset()

    def check_players(self):
        if self.distance(self.player1) <= 25 or self.distance(self.player2) <= 25:
            self.setheading(180 - self.heading())
