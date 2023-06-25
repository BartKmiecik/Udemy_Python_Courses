from turtle import Screen, Turtle

tim = Turtle()
tim.shape("turtle")
tim.color("red")

for _ in range(10):
    tim.pd()
    tim.forward(10)
    tim.pu()
    tim.forward(10)


screen = Screen()
screen.exitonclick()