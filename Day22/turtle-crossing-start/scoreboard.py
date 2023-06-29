from turtle import Turtle
FONT = ("Courier", 22, "normal")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.pu()
        self.color('black')
        self.goto(-220, 250)
        self.level = 1
        self.write(f'Level {self.level}', False, 'center', FONT)

    def update_level(self):
        self.level += 1
        self.clear()
        self.write(f'Level {self.level}', False, 'center', FONT)

    def game_over(self):
        self.goto(0, 0)
        self.write(f'Game Over', False, 'center', FONT)
