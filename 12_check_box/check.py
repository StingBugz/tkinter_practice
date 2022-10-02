from tkinter import *

root = Tk()
root.title("Check box App")
root.geometry("400x400")

def event_resize():
    if var.get() == "yes":
        Label(root, text="resized").pack()
        root.geometry("200x200")
    else:
        Label(root, text="default").pack()
        root.geometry("400x400")

# var = IntVar()  this is for integer variable in checkbox
var = StringVar()

check = Checkbutton(root, text="200 x x200", variable=var, onvalue="yes", offvalue="no")
check.deselect() #to deselect the checkbox by default
btn_change = Button(root, text="resize", command=event_resize)

check.pack()
btn_change.pack()

root.mainloop()