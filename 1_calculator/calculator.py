import math
from tkinter import *

root = Tk()
root.title("simple calculator")
icon = PhotoImage(file="/home/yatora/Documents/tkinter_practice_linux/source/favicon/calculator.png")
root.tk.call("wm","iconphoto", root._w, icon)
def event_click(number):
    current = e.get()
    e.delete(0, END)
    e.insert(0, str(current) + str(number))

def event_equal():
    second_num = e.get()
    e.delete(0, END)
    if math == "addition":
        e.insert(0, int(first_num) + int(second_num))
    
    if math == "subtract":
        e.insert(0, int(first_num) - int(second_num))
    
    if math == "multiply":
        e.insert(0, int(first_num) * int(second_num))
    
    if math == "divide":
        e.insert(0, int(first_num) / int(second_num))


def event_clear():
    e.delete(0, END)

def event_add():
    global first_num
    global math
    math = 'addition'
    first_num = int(e.get())
    e.delete(0, END)


def event_subtract():
    global first_num
    global math
    math = 'subtract'
    first_num = int(e.get())
    e.delete(0, END)

def event_multiply():
    global first_num
    global math
    math = 'multiply'
    first_num = int(e.get())
    e.delete(0, END)

def event_divide():
    global first_num
    global math
    math = 'divide'
    first_num = int(e.get())
    e.delete(0, END)

e = Entry(root, bd=4, relief=SUNKEN, width=30)
btn9 = Button(root, text="9",width=4,height=3, command=lambda:event_click(9))
btn8 = Button(root, text="8",width=4,height=3, command=lambda:event_click(8))
btn7 = Button(root, text="7",width=4,height=3, command=lambda:event_click(7))
btn6 = Button(root, text="6",width=4,height=3, command=lambda:event_click(6))
btn5 = Button(root, text="5",width=4,height=3, command=lambda:event_click(5))
btn4 = Button(root, text="4",width=4,height=3, command=lambda:event_click(4))
btn3 = Button(root, text="3",width=4,height=3, command=lambda:event_click(3))
btn2 = Button(root, text="2",width=4,height=3, command=lambda:event_click(2))
btn1 = Button(root, text="1",width=4,height=3, command=lambda:event_click(1))
btn0 = Button(root, text="0",width=4,height=3, command=lambda:event_click(0))

btn_clear = Button(root, text="C",width=4,height=3, command=event_clear)
btn_add = Button(root, text="+",width=4,height=3, command=event_add)
btn_subtract = Button(root, text="-",width=4,height=3, command=event_subtract)
btn_multiply = Button(root, text="x",width=4,height=3, command=event_multiply)
btn_divide = Button(root, text=":",width=4,height=3, command=event_divide)
btn_equal = Button(root, text="=", width=4, height=3, command=event_equal)

e.grid(row=0, column=0, columnspan=4)
btn9.grid(row=1, column=2)
btn8.grid(row=1, column=1)
btn7.grid(row=1, column=0)
btn6.grid(row=2, column=2)
btn5.grid(row=2, column=1)
btn4.grid(row=2, column=0)
btn3.grid(row=3, column=2)
btn2.grid(row=3, column=1)
btn1.grid(row=3, column=0)
btn0.grid(row=4, column=1)

btn_clear.grid(row=4, column=0)
btn_add.grid(row=4, column=2)
btn_subtract.grid(row=3, column=3)
btn_multiply.grid(row=2, column=3)
btn_divide.grid(row=1, column=3)
btn_equal.grid(row=4, column=3)

root.mainloop()