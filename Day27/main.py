from tkinter import *

window = Tk()
#window.minsize(200, 100)
window.title('Miles to km conventer.')
window.config(padx=20, pady=20)

entry = Entry(width=5)
entry.grid(column=2, row=0)

label = Label(text='Miles:', width=10)
label.grid(columns=1, row=0)

label2 = Label(text='is equal to')
label2.grid(column=0, row=1)

result = Label(text='0')
result.grid(column=1,row=1)

label3 = Label(text="Km")
label3.grid(column=2,row=1)

def calulate_miles_to_km():
    miles = float(entry.get())
    km = miles * 1.6
    result.config(text =str(km))

button = Button(text='Calculate')
button.grid(column=1,row=2)
button.config(command=calulate_miles_to_km)


window.mainloop()