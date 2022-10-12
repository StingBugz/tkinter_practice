from logging import root
from tkinter import *
import numpy as np
import matplotlib.pyplot as plot

root = Tk()
root.title("Chart App")
icon_root = PhotoImage(file="./source/favicon/chart.png")
root.tk.call("wm","iconphoto", root._w, icon_root)
root.geometry("50x50")

def chart():
    dummy_data = np.random.normal(loc=1000,scale=50,size=20)
    plot.hist(dummy_data,20)
    plot.show()


btn_show = Button(root, text="Charts", command=chart)
btn_show.pack()
root.mainloop()