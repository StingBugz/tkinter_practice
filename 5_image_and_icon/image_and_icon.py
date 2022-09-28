from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title("show Images")
root.iconbitmap("d:/Python/source/jp.ico")

quit_btn = Button(root, text="exit", bg="red", fg="white", command=root.quit)
my_img = ImageTk.PhotoImage(Image.open("../source/cat_smudge.jpg"))
my_label = Label(root, image=my_img)


my_label.pack()
quit_btn.pack()
root.mainloop()