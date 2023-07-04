from tkinter import *

THEME_COLOR = "#375362"

class UiWindow():

    def __init__(self):
        window = Tk()
        window.title('Quizzler')
        window.config(bg=THEME_COLOR, pady=100, padx=20)

        canvas = Canvas()
        rect_canvas = canvas.create_rectangle(0, 0, 500, 300,outline='white')
        question_text = canvas.create_text(200, 100, text='lorem ipsum traterate',
                                           fill='black', font=('Helvetica', 16) )
        canvas.grid(row=1, column=0, columnspan=2, pady=50)
        score_text = Label(text='Score 0', foreground='white', bg=THEME_COLOR)
        score_text.grid(row=0, column=1)


        def correct(self):
            pass

        correct_img = PhotoImage(file='images/true.png')
        correct_btn = Button(image=correct_img, command=correct)
        correct_btn.grid(row=2, column=0)

        def incorrect(self):
            pass

        wrong_img = PhotoImage(file='images/false.png')
        wrong_btn = Button(image=wrong_img, command=incorrect)
        wrong_btn.grid(row=2, column=1)

        window.mainloop()


wind = UiWindow()