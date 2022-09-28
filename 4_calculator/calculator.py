from tkinter import *
from math import *

root = Tk()
root.title('Simple Calculator')
def event_click(number):
    current = e.get()
    e.delete(0, END)
    e.insert(0, str(current) + str(number))

def event_mod():
    first_number = e.get()
    global f_num
    global math
    math = "modulus"
    f_num = int(first_number)
    e.delete(0, END)

def event_division():
    first_number = e.get()
    global f_num
    global math
    math = "division"
    f_num = int(first_number)
    e.delete(0, END)
def event_multiply():
    first_number = e.get()
    global f_num
    global math
    math = "multiplication"
    f_num = int(first_number)
    e.delete(0, END)
def event_subtraction():
    first_number = e.get()
    global f_num
    global math
    math = "subtraction"
    f_num = int(first_number)
    e.delete(0, END)
def event_addition():
    first_number = e.get()
    global f_num
    global math
    math = "addition"
    f_num = int(first_number)
    e.delete(0, END)

def event_clear():
    e.delete(0, END)

def event_equal():
    second_number = e.get()
    e.delete(0, END)
    if math == "addition":
        e.insert(0, f_num + int(second_number))
    if math == "subtraction":
        e.insert(0, f_num - int(second_number))
    if math == "multiplication":
        e.insert(0, f_num * int(second_number))
    if math == "division":
        e.insert(0, floor(f_num / int(second_number)))
    if math == "modulus":
        e.insert(0, f_num % int(second_number))



#init text box
e = Entry(root, width=50, borderwidth=5)

#init button
button_1 = Button(root, text='1', padx=40, pady=20, command=lambda: event_click(1))
button_2 = Button(root, text='2', padx=40, pady=20, command=lambda: event_click(2))
button_3 = Button(root, text='3', padx=40, pady=20, command=lambda: event_click(3))
button_4 = Button(root, text='4', padx=40, pady=20, command=lambda: event_click(4))
button_5 = Button(root, text='5', padx=40, pady=20, command=lambda: event_click(5))
button_6 = Button(root, text='6', padx=40, pady=20, command=lambda: event_click(6))
button_7 = Button(root, text='7', padx=40, pady=20, command=lambda: event_click(7))
button_8 = Button(root, text='8', padx=40, pady=20, command=lambda: event_click(8))
button_9 = Button(root, text='9', padx=40, pady=20, command=lambda: event_click(9))
button_0 = Button(root, text='0', padx=40, pady=60, command=lambda: event_click(0))
button_add = Button(root, text='+', padx=37, pady=20, command=event_addition)
button_subtract = Button(root, text='-', padx=40, pady=20, command=event_subtraction)
button_division = Button(root, text=':', padx=40, pady=20, command=event_division)
button_multiple = Button(root, text='x', padx=40, pady=20, command=event_multiply)
button_mod = Button(root, text='%', padx=38, pady=10, command=event_mod)
button_equal = Button(root, text='=', padx=39, pady=10, command=event_equal)
button_clear = Button(root, text='clear', padx=31, pady=10, command=event_clear)


#text box
e.grid(row=0, column=0, columnspan=3)
#button
button_9.grid(row=1, column=2, columnspan=1, pady=5, padx=3)
button_8.grid(row=1, column=1, columnspan=1, pady=5)
button_7.grid(row=1, column=0, columnspan=1, pady=5)

button_6.grid(row=2, column=2, columnspan=1, pady=5, padx=3)
button_5.grid(row=2, column=1, columnspan=1, pady=5)
button_4.grid(row=2, column=0, columnspan=1, pady=5)

button_3.grid(row=3, column=2, columnspan=1, pady=5, padx=3)
button_2.grid(row=3, column=1, columnspan=1, pady=5)
button_1.grid(row=3, column=0, columnspan=1, pady=5)

button_0.grid(row=4, column=0, rowspan=2, padx=3)


button_add.grid(row=4, column=1, padx=5, pady=3)
button_subtract.grid(row=4, column=2, padx=3, pady=3)

button_division.grid(row=5, column=1, padx=3, pady=3)
button_multiple.grid(row=5, column=2, padx=3, pady=3)

button_equal.grid(row=6, column=2, padx=5, pady=3)
button_clear.grid(row=6, column=0, padx=5, pady=3)
button_mod.grid(row=6, column=1, pady=3)


root.mainloop()