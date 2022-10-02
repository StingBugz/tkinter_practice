from tkinter import *

root = Tk()
root.title("Slider App")
root.geometry("400x400")

def event_slide():
    root.geometry(f"{horizontal.get()}x{vertical.get()}")


label_vertical = Label(root, text="vertical")
label_horizontal = Label(root,text="horizontal")
vertical = Scale(root, from_=0, to=400)
horizontal = Scale(root, from_=0, to=400, orient=HORIZONTAL)


btn_change = Button(root, text="Resize", command=event_slide)

label_vertical.pack()
vertical.pack()
label_horizontal.pack()
horizontal.pack()
btn_change.pack()

root.mainloop()