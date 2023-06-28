from turtle import Turtle
import random
class Food(Turtle):

    def __init__(self):
        super().__init__()
        #self.food = Turtle()
        self.pu()
        self.spawn_food()
        self.color('green')
        self.shapesize(.7, .7)
        self.shape('circle')

    def spawn_food(self):
        x, y = random.randint(-290, 290), random.randint(-290, 290)
        self.goto(x, y)
