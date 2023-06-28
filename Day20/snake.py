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

    def add_body(self):
        turtle = Turtle()
        turtle.pu()
        turtle.shape('square')
        temp = self.turtles[-1]
        turtle.goto(temp.pos()[0], temp.pos()[1])
        turtle.color('white')
        self.turtles.append(turtle)

    def update(self):
        for t in range(len(self.turtles) - 1, 0, -1):
            pos = self.turtles[t - 1].pos()
            self.turtles[t].goto(pos[0], pos[1])
        self.head.forward(20)

    def move_up(self):
        if self.head.heading() != 270:
            self.head.setheading(90)

    def move_down(self):
        if self.head.heading() != 90:
            self.head.setheading(270)

    def move_right(self):
        if self.head.heading() != 180:
            self.head.setheading(0)

    def move_left(self):
        if self.head.heading() != 0:
            self.head.setheading(180)


