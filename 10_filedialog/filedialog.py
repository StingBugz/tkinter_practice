from tkinter import *
from PIL import ImageTk, Image
from tkinter import filedialog
root = Tk()
root.title("template")
icon = PhotoImage(file="./source/favicon/jp_flag.png")
root.tk.call("wm", "iconphoto", root._w, icon)

def event_open_file():
    global img
    root.filename = filedialog.askopenfilename(initialdir="D:/Python/source",title="Open Image", filetypes=(("jpg files","*.jpg"),("all files","*.*")))
    Label(root, text=root.filename).pack()
    img = ImageTk.PhotoImage(Image.open(root.filename))
    Label(image=img).pack()
    Button(root, text="exit program",command=root.quit).pack()

Button(root, text="Open File", command=event_open_file).pack()


root.mainloop()