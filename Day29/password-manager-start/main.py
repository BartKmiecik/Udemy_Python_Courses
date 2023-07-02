from tkinter import *
# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #

# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title('Password saver')
window.minsize(width=200, height=200)
window.config(pady=20, padx=20)

canvas = Canvas(width=300, height=200)
logo_file = PhotoImage(file='logo.png')
canvas.create_image(100, 100, image=logo_file)
canvas.grid(column=1, row=0)

web_label = Label(text='Website: ', width= 10)
web_label.grid(column=0, row=1)

user_label = Label(text='Email/Username:', width=10)
user_label.grid(column=0, row=2)

password_label = Label(text='Password:', width=10)
password_label.grid(column=0, row=3)

web_entry = Entry(width=30)
web_entry.grid(column=1,row=1)

user_entry = Entry(width=30, text='mypassword@phuck.com')
user_entry.grid(column=1, row=2)

pass_entry = Entry(width=10)
pass_entry.grid(column=1, row=3)

def pass_generate():
    pass

gen_pass_btn = Button(text='Generate Password', width=10 ,command=pass_generate)
gen_pass_btn.grid(column=2, row=3)

def add_fn():
    pass

add_btn = Button(text='Add', width=30)
add_btn.grid(column=1, row=4)

window.mainloop()