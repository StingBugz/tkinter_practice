from tkinter import *

#main window
root = Tk()

#create label
label1 = Label(root, text="hello world!").grid(row=0,column=1)
label2 = Label(root, text="hello my name is syarif").grid(row=0,column=2)

#packing all the widget
# label1.grid(row=0,column=0)
# label2.grid(row=1,column=0)

#mainloop
root.mainloop()