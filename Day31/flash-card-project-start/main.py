from tkinter import *
import pandas as pd
import random
import time
BACKGROUND_COLOR = "#B1DDC6"
#---------------------Logic----------------------------
title_text = 'Language'
word_text = 'word'
counter = 0
data = pd.read_csv('data/french_words.csv')
to_learn = data.to_dict(orient='records')
def right_answer():
    to_learn.remove(to_learn[counter])
    next_word()


def wrong_answer():
    next_word()

def show_answer():
    canvas.itemconfig(flash_card_img, image=back_img)
    title_text = 'English'
    word_text = f'{to_learn[counter]["English"]}'
    canvas.itemconfig(lang_canvas, text=title_text)
    canvas.itemconfig(word_canvas, text=word_text)

def next_word():
    global counter, flip_timer
    window.after_cancel(flip_timer)
    canvas.itemconfig(flash_card_img, image=front_img)
    counter = random.randint(0, len(to_learn) - 1)
    title_text = 'French'
    word_text = f'{to_learn[counter]["French"]}'
    canvas.itemconfig(lang_canvas, text=title_text)
    canvas.itemconfig(word_canvas, text=word_text)
    flip_timer= window.after(3000, show_answer)




#---------------------UI-------------------------------
window = Tk()
window.config(padx=200, pady=200, bg= BACKGROUND_COLOR, borderwidth=0)
window.minsize(width=800, height=550)
window.title('Flashcards')

front_img = PhotoImage(file='images/card_front.png')
back_img = PhotoImage(file='images/card_back.png')

canvas = Canvas(width=800, height=550)
card_front_img = PhotoImage(file='images/card_front.png')
flash_card_img = canvas.create_image(400, 270, image=card_front_img)
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

flip_timer = window.after(3000, show_answer)
next_word()


window.mainloop()