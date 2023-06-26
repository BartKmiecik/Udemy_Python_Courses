from turtle import Turtle, Screen
import random

screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput('Winner','Who\'s gonna win?')

colors = ['violet', 'orange', 'brown', 'red', 'green', 'yellow']
def get_random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return r, g, b

tortoises = []
for i in range(6):
    tim = Turtle()
    tim.pu()
    tim.shape('turtle')
    tim.speed()
    color = colors[i]
    tim.color(color)
    tortoises.append(tim)

for i, t in enumerate(tortoises):
    t.goto(-220, -150 + (50 * i))

winner = ''
while len(winner) < 1:
    for t in tortoises:
        t.forward(random.randint(10, 30))
        if t.pos()[0] > 240:
            winner = t.color()

if user_bet == winner:
    print(f'Congratulation {user_bet} won!')
else:
    print(f'You lose, {winner} won!')

screen.exitonclick()