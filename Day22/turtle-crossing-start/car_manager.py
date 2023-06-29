from turtle import Turtle
import random
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 30
MOVE_INCREMENT = 10


class CarManager(Turtle):

    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.cars = []
        for i in range(15):
            car = Turtle()
            car.pu()
            car.shape('square')
            car.shapesize(1, 2)
            car.setheading(180)
            car.color(COLORS[random.randint(0, len(COLORS) - 1)])
            car.goto(320 + i * STARTING_MOVE_DISTANCE, random.randint(-250, 250))
            self.cars.append(car)
        self.level = 1

    def update(self):
        for car in self.cars:
            car.forward(MOVE_INCREMENT * self.level)
            if(car.pos()[0] < - 300):
                car.goto(320, random.randint(-250, 250))

    def reset(self) -> None:
        for i in range(15):
            self.cars[i].goto(320 + i * STARTING_MOVE_DISTANCE, random.randint(-250, 250))

    def increase_level(self):
        self.level += 1
        self.reset()