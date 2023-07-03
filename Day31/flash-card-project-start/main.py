from tkinter import *
BACKGROUND_COLOR = "#B1DDC6"
#---------------------Logic----------------------------

def right_answer():
    pass

def wrong_answer():
    pass

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

wrong_img = PhotoImage(file='images/wrong.png')
wrong_button = Button(image=wrong_img, highlightthickness=0,borderwidth=0, command=wrong_answer)
wrong_button.grid(column=0, row=2)

right_img = PhotoImage(file='images/right.png')
right_button = Button(image=right_img, highlightthickness=0, borderwidth=0, command=right_answer)
right_button.grid(column=2, row=2)

window.mainloop()