from turtle import Turtle
class Snake():
    def __init__(self):
        self.turtles = []
        for i in range(3):
            turtle = Turtle()
            turtle.pu()
            turtle.shape('square')
            turtle.goto(0 - i * 20, 0)
            turtle.color('white')
            self.turtles.append(turtle)
        self.head = self.turtles[0]

    def update(self):
        for t in range(len(self.turtles) - 1, 0, -1):
            pos = self.turtles[t - 1].pos()
            self.turtles[t].goto(pos[0], pos[1])
        self.head.forward(20)
