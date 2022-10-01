from tkinter import *
from tkinter.ttk import Labelframe
root = Tk()
root.title("template")
icon = PhotoImage(file="./source/favicon/radio.png")
root.tk.call("wm", "iconphoto", root._w, icon)

def event_choose(topping):
    Label(frame, text=topping).pack()


toppings = [
    ("Booba","Booba"),
    ("Chocolate", "Chocolate"),
    ("Oreo", "Oreo"),
    ("Milk","Milk")
]

frame = Labelframe(root, padding="10")
frame.pack(pady=5, padx=10)

drink = StringVar()
drink.set("0")

for text, topping in toppings:
    Radiobutton(frame, text=text, variable=drink, value=topping).pack(anchor=W)


btn_choose = Button(frame, text="Choose",command=lambda:event_choose(drink.get()))
btn_choose.pack()


root.mainloop()