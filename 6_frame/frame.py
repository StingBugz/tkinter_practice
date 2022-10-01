from tkinter import *
root = Tk()
root.title("frame")
icon = PhotoImage(file="./source/favicon/jp_flag.png")
root.tk.call("wm", "iconphoto", root._w, icon)

frame = LabelFrame(root, text="This is frame")
frame.pack(pady=30, padx=30)

btn1 = Button(frame, text="Don't Click Here !!!", command=root.quit)
btn1.grid(row=0,column=0, padx=20, pady=20)

root.mainloop()