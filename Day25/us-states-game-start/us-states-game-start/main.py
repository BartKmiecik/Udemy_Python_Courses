import turtle

import pandas as pd
from turtle import Turtle, Screen
data = pd.read_csv('50_states.csv')
unique_states = data['state'].tolist()
screen = Screen()
screen.title('USA')
image = 'blank_states_img.gif'
screen.addshape(image)
turtle.shape(image)
turtle = Turtle()
turtle.pu()
turtle.hideturtle()


while True:
    i = len(data) - len(unique_states)
    prompt = screen.textinput(f'States {i}/50', 'Give me name of the states')
    if data['state'].unique().__contains__(prompt):
        if unique_states.__contains__(prompt):
            unique_states.remove(prompt)
            x = data.loc[data['state'] == prompt]['x'].item()
            y = data.loc[data['state'] == prompt]['y'].item()
            turtle.goto(x,y)
            turtle.write(prompt, False, 'center')

screen.exitonclick()