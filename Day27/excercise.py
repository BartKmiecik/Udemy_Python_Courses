from tkinter import *

tk = Tk()
tk.title('Gui Example')
tk.minsize(600, 300)

label = Label(text ='Some text')
label.grid(column = 0, row = 0)

def button_command():
    text = entry.get()
    label.config(text = text)

button = Button(text = 'Click me', command=button_command)
button.grid(column = 1, row= 1)

button2 = Button(text = 'Second BTN')
button2.grid(column=2, row= 0)

entry = Entry(text = 'Write here!')
entry.grid(column= 4, row= 4)


tk.mainloop()