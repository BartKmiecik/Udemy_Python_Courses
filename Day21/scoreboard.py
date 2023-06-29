from turtle import  Turtle

class Scoreboard(Turtle):

    def __init__(self, is_player : bool):
        super().__init__()
        self.pu()
        self.hideturtle()
        self.color('white')
        x = 70 if is_player else - 70
        self.goto(x, 240)
        self.score = 0
        self.write(f'{self.score}', False, 'center', ('Ariel', 28, 'bold'))


    def get_point(self):
        self.clear()
        self.score += 1
        self.write(f'{self.score}', False, 'center', ('Ariel', 28, 'bold'))
