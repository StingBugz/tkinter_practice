from tkinter import *

root = Tk()
root.title('Simple Calculator')
def event_click(number):
    current = e.get()
    e.delete(0, END)
    e.insert(0, str(current) + str(number))

def event_clear():
    e.delete(0, END)

def event_add():
    first_number = e.get()
    global f_num
    f_num = int(first_number)
    e.delete(0, END)

def event_equal():
    second_number = e.get()
    e.delete(0, END)
    e.insert(0, f_num + int(second_number))


e = Entry(root, width=50, borderwidth=5)

button_1 = Button(root, text='1', padx=40, pady=20, command=lambda: event_click(1))
button_2 = Button(root, text='2', padx=40, pady=20, command=lambda: event_click(2))
button_3 = Button(root, text='3', padx=40, pady=20, command=lambda: event_click(3))
button_4 = Button(root, text='4', padx=40, pady=20, command=lambda: event_click(4))
button_5 = Button(root, text='5', padx=40, pady=20, command=lambda: event_click(5))
button_6 = Button(root, text='6', padx=40, pady=20, command=lambda: event_click(6))
button_7 = Button(root, text='7', padx=40, pady=20, command=lambda: event_click(7))
button_8 = Button(root, text='8', padx=40, pady=20, command=lambda: event_click(8))
button_9 = Button(root, text='9', padx=40, pady=20, command=lambda: event_click(9))
button_0 = Button(root, text='0', padx=40, pady=80, command=lambda: event_click(0))
button_add = Button(root, text='+', padx=37, pady=20, command=event_add)
button_subtract = Button(root, text='-', padx=40, pady=20, command=lambda: event_click(9))
button_division = Button(root, text=':', padx=40, pady=20, command=lambda: event_click(9))
button_multiple = Button(root, text='x', padx=40, pady=20, command=lambda: event_click(9))
button_clear = Button(root, text='clear', padx=30, pady=10, command=event_clear)
button_equal = Button(root, text='=', padx=40, pady=10, command=event_equal)

e.grid(row=0, column=0, columnspan=3)
button_9.grid(row=1, column=2, columnspan=1, pady=5, padx=5)
button_8.grid(row=1, column=1, columnspan=1, pady=5)
button_7.grid(row=1, column=0, columnspan=1, pady=5)

button_6.grid(row=2, column=2, columnspan=1, pady=5, padx=5)
button_5.grid(row=2, column=1, columnspan=1, pady=5)
button_4.grid(row=2, column=0, columnspan=1, pady=5)

button_3.grid(row=3, column=2, columnspan=1, pady=5, padx=5)
button_2.grid(row=3, column=1, columnspan=1, pady=5)
button_1.grid(row=3, column=0, columnspan=1, pady=5)

button_0.grid(row=4, column=0, rowspan=3, padx=5)

button_add.grid(row=4, column=1, padx=5, pady=3)
button_subtract.grid(row=4, column=2, padx=5, pady=3)

button_division.grid(row=5, column=1, padx=5, pady=3)
button_multiple.grid(row=5, column=2, padx=5, pady=3)

button_equal.grid(row=6, column=1, padx=5, pady=3)
button_clear.grid(row=6, column=2, padx=5, pady=3)


root.mainloop()