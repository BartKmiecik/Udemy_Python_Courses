from turtle import Turtle

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.points = 0
        self.hideturtle()
        self.pu()
        self.color('white')
        self.goto(0, 300)
        self.write(f'Score {self.points}', False, 'center', ('Ariel', 20, 'normal'))


    def game_over(self):
        self.goto(0, 0)
        self.write(f'Game Over', False, 'center', ('Ariel', 48, 'normal'))

    def update_score(self):
        self.clear()
        self.points += 1
        self.write(f'Score {self.points}', False, 'center', ('Ariel', 20, 'normal'))