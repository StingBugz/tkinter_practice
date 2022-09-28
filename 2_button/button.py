from tkinter import *
from unittest import result 


def clickMe():
    a = 1
    b = 2
    result = a + b
    label1 = Label(root,text=result)
    label1.pack()

root = Tk()

button1 = Button(root,text="Click me!",command=clickMe, fg="red", bg="white") #state for disable and enable button
button1.pack()

root.mainloop()