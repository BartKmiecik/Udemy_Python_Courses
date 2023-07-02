from tkinter import *
import time
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
CYCLES = 7
window_timer = None
# ---------------------------- TIMER RESET ------------------------------- #
def reset_fn():
    global cycles
    global should_count
    global check_text
    window.after_cancel(window_timer)
    canvas.itemconfig(counter_txt, text='00:00')
    check_text = ''
    checkmark.config(text= check_text)
    cycles = 0
    should_count = False

# ---------------------------- TIMER MECHANISM ------------------------------- #
time_passed = 0
cycles = 0
should_count = False
check_text = ''
def start_fn():
    global cycles
    global should_count
    global window_timer
    if cycles == 0 & should_count == False:
        should_count = True
    if cycles % 2 == 0 and cycles < CYCLES:
        change_cycle = counter(WORK_MIN)
        title.config(text='Work', fg=GREEN)
    elif cycles < CYCLES:
        change_cycle = counter(SHORT_BREAK_MIN)
        title.config(text='Short Break', fg=RED)
    elif cycles == CYCLES:
        change_cycle = counter(LONG_BREAK_MIN)
        title.config(text='Long Break')

    if change_cycle:
        cycles += 1

    if change_cycle and cycles > CYCLES:
        return
    if should_count:
        window_timer = window.after(1000, start_fn)

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def counter(timer):
    global time_passed
    global check_text
    timer = timer * 60
    minutes = int((timer - time_passed) / 60)
    sec = int((timer - time_passed) % 60)
    if sec < 10:
        sec = '0' + str(sec)
    canvas.itemconfig(counter_txt, text=f'{minutes}:{sec}')
    time_passed += 1
    if time_passed > timer:
        time_passed = 0
        check_text += '✓'
        checkmark.config(text=check_text)
        return True
    else:
        return False

# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title('Pomodoro')
window.config(padx=100, pady=50, bg=YELLOW)

canvas = Canvas(bg = YELLOW, highlightthickness=0, height=240, width=240)
tom_img = PhotoImage(file='tomato.png')
canvas.create_image(100, 112, image=tom_img)
counter_txt = canvas.create_text(100, 130, text='00:00', fill='white', font=(FONT_NAME,35,'bold'))
canvas.grid(column=1, row=1)


start_btn = Button(text='Start', command=start_fn)
start_btn.grid(column=0, row=2)


reset_btn = Button(text='Reset', command=reset_fn)
reset_btn.grid(column=2, row=2)

title = Label(text='Timer', fg=GREEN, bg=YELLOW,
              font=(FONT_NAME, 42, 'bold'))
title.grid(column=1, row=0)

checkmark = Label(text='', fg=GREEN, bg=YELLOW)
checkmark.grid(column=1, row=3)


window.mainloop()