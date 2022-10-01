from tkinter import *
root = Tk()
root.title("template")
icon = PhotoImage(file="./source/favicon/")
root.tk.call("wm", "iconphoto", root._w, icon)


root.mainloop()