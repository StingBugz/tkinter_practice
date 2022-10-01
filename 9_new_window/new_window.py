from tkinter import *
from PIL import ImageTk, Image
root = Tk()
root.title("template")
icon = PhotoImage(file="./source/favicon/window.png")
root.tk.call("wm", "iconphoto", root._w, icon)

def event_open():
    global img
    top = Toplevel()
    img = ImageTk.PhotoImage(Image.open("D:/Python/source/img/cat_meme2.jpg"))
    Label(top,image=img).pack()
    Button(top, text="Close Window", command=top.destroy).pack()


btn_new = Button(root, text="Open New Window", command=event_open).pack()


root.mainloop()