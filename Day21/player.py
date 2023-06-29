from turtle import  Turtle
from scoreboard import Scoreboard
class Player(Turtle):

    def __init__(self, is_player: bool):
        super().__init__()
        self.pu()
        self.shape('square')
        self.color('white')
        self.shapesize(1, 3)
        self.setheading(90)
        x = 280 if is_player else - 280
        self.goto(x, 0)
        self.scoreboard = Scoreboard(is_player)


    def move_up(self):
        if self.pos()[1] < 270:
            self.forward(10)

    def move_down(self):
        if self.pos()[1] > -260:
            self.backward(10)

    def get_Point(self):
        self.scoreboard.get_point()

