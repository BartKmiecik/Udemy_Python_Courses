from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"

class UiWindow():

    def __init__(self, quizz_brain: QuizBrain):
        self.quizz_brain = quizz_brain
        self.window = Tk()
        self.window.title('Quizzler')
        self.window.config(bg=THEME_COLOR, pady=100, padx=20)

        self.canvas = Canvas(width=300, height=250, bg='white')
        #self.rect_canvas = self.canvas.create_rectangle(0, 0, 300, 250,outline='white')
        self.question_text = self.canvas.create_text(150, 125, text='lorem ipsum traterate',
                                           fill=THEME_COLOR, font=('Helvetica', 16), width= 250)
        self.canvas.grid(row=1, column=0, columnspan=2, pady=50)
        self.score_text = Label(text='Score 0', foreground='white', bg=THEME_COLOR)
        self.score_text.grid(row=0, column=1)
        self.score = 0

        self.correct_img = PhotoImage(file='images/true.png')
        self.correct_btn = Button(image=self.correct_img, command=self.correct)
        self.correct_btn.grid(row=2, column=0)


        self.wrong_img = PhotoImage(file='images/false.png')
        self.wrong_btn = Button(image=self.wrong_img, command=self.incorrect)
        self.wrong_btn.grid(row=2, column=1)

        self.next_question()

        self.window.mainloop()

    def correct(self):
        self.next_question()
        self.score = self.quizz_brain.check_answer(True)
        self.score_text.config(text=f'Score {self.score}')
        print(self.score)


    def incorrect(self):
        self.next_question()
        self.score = self.quizz_brain.check_answer(False)
        self.score_text.config(text=f'Score {self.score}')
        print(self.score)


    def next_question(self):
        next = self.quizz_brain.next_question()
        self.canvas.itemconfig(self.question_text, text=next)



