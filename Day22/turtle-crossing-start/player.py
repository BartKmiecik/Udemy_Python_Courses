from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):

    def __init__(self):
        super().__init__()
        self.pu()
        self.shape('turtle')
        self.goto(0,-280)
        self.color('black')
        self.setheading(90)

    def move_forward(self):
        self.forward(10)

    def reset(self) -> None:
        self.goto(0, -280)
