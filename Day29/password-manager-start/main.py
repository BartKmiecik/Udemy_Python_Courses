from tkinter import *
from tkinter import messagebox
from password_generator import Password_generator
import pyperclip
# ---------------------------- PASSWORD GENERATOR ------------------------------- #


def pass_generate():
    generator = Password_generator()
    pass_entry.delete(0, END)
    password = generator.get_password()
    pass_entry.insert(0, password)
    pyperclip.copy(password)
    
# ---------------------------- SAVE PASSWORD ------------------------------- #
def add_fn():
    web = web_entry.get()
    user = user_entry.get()
    password = pass_entry.get()
    if len(web) <= 0 or len(user) <= 0 or len(password) <= 0:
        messagebox.showinfo('Warrning','You left some empty entries!')
        print('Missing some filed!')
        return

    should_save = messagebox.askokcancel(title=web, message=f'Are you sure you want to save {password} to {user}?')
    if should_save:
        with open('passwords.txt', 'a') as file:
            file.write(f'{web} | {user} | {password}\n')
            print('Succesfully saved')
            web_entry.delete(0, END)
            pass_entry.delete(0, END)


# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title('Password saver')
window.minsize(width=200, height=200)
window.config(pady=20, padx=20)

canvas = Canvas(width=200, height=200)
logo_file = PhotoImage(file='logo.png')
canvas.create_image(100, 100, image=logo_file)
canvas.grid(column=1, row=0)

web_label = Label(text='Website: ')
web_label.grid(column=0, row=1)

user_label = Label(text='Email/Username:')
user_label.grid(column=0, row=2)

password_label = Label(text='Password:')
password_label.grid(column=0, row=3)

web_entry = Entry(width=39)
web_entry.focus()
web_entry.grid(column=1,row=1, columnspan=2)

user_entry = Entry(width=39)
user_entry.insert(0,'mypassword@phuck.com')
user_entry.grid(column=1, row=2, columnspan=2)

pass_entry = Entry(width=21)
pass_entry.grid(column=1, row=3)



gen_pass_btn = Button(text='Generate Password' ,command=pass_generate)
gen_pass_btn.grid(column=2, row=3)


add_btn = Button(text='Add', width=36, command=add_fn)
add_btn.grid(column=1, row=4,columnspan=2)

window.mainloop()