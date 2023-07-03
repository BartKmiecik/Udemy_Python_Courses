from tkinter import *
import pandas as pd
import random
BACKGROUND_COLOR = "#B1DDC6"
#---------------------Logic----------------------------
title_text = 'Language'
word_text = 'word'

data = pd.read_csv('data/french_words.csv')

def right_answer():
    i = random.randint(0, len(data)-1)
    title_text = 'French'
    word_text = f'{data.iloc[i]["French"]}'
    canvas.itemconfig(lang_canvas, text=title_text)
    canvas.itemconfig(word_canvas, text=word_text)


def wrong_answer():
    i = random.randint(0, len(data) - 1)
    title_text = 'French'
    word_text = f'{data.iloc[i]["French"]}'
    canvas.itemconfig(lang_canvas, text=title_text)
    canvas.itemconfig(word_canvas, text=word_text)


#---------------------UI-------------------------------
window = Tk()
window.config(padx=200, pady=200, bg= BACKGROUND_COLOR, borderwidth=0)
window.minsize(width=800, height=550)
window.title('Flashcards')

canvas = Canvas(width=800, height=550)
image = PhotoImage(file='images/card_front.png')
canvas.create_image(400, 270, image=image)
canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0, border=0)
canvas.grid(column=1, row=1)
lang_canvas = canvas.create_text(400,200, text= title_text, fill='black', font=('Arial', 24, 'bold'))
word_canvas = canvas.create_text(400,270, text= word_text, fill='black', font=('Arial', 24, 'bold'))


wrong_img = PhotoImage(file='images/wrong.png')
wrong_button = Button(image=wrong_img, highlightthickness=0,borderwidth=0, command=wrong_answer)
wrong_button.grid(column=0, row=2)

right_img = PhotoImage(file='images/right.png')
right_button = Button(image=right_img, highlightthickness=0, borderwidth=0, command=right_answer)
right_button.grid(column=2, row=2)

window.mainloop()