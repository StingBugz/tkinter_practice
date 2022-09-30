from tkinter import *
from PIL import ImageTk, Image


root = Tk()
root.title("show Images")
# root.iconbitmap("../source/favicon/jp.ico")
icon = PhotoImage(file="D:/Python/source/favicon/jp_flag.png")
root.tk.call('wm','iconphoto',root._w,icon)




img1 = ImageTk.PhotoImage(Image.open("D:/Python/source/img/cat_meme1.jpg"))
img2 = ImageTk.PhotoImage(Image.open("D:/Python/source/img/cat_meme2.jpg"))
img3 = ImageTk.PhotoImage(Image.open("D:/Python/source/img/cat_meme3.jpg"))
img4 = ImageTk.PhotoImage(Image.open("D:/Python/source/img/cat_meme4.jpg"))
img5 = ImageTk.PhotoImage(Image.open("D:/Python/source/img/cat_meme5.jpg"))
img6 = ImageTk.PhotoImage(Image.open("D:/Python/source/img/cat_meme6.jpg"))


img_list = [img1, img2, img3, img4, img5, img6]

def event_forward(number_image):
    global my_label
    global forward_btn
    global back_btn

    my_label.grid_forget()
    my_label = Label(image=img_list[number_image - 1])

    back_btn = Button(root, text="<<", command=lambda:event_back(number_image - 1))
    forward_btn = Button(root, text=">>", command=lambda:event_forward(number_image + 1))
    if number_image == 5:
         forward_btn = Button(root, text=">>", state=DISABLED)

    my_label.grid(row=0, column=0, columnspan=3)
    back_btn.grid(row=1, column=0)
    forward_btn.grid(row=1, column=2)
def event_back(number_image):
    global my_label
    global forward_btn
    global back_btn

    my_label.grid_forget()
    my_label = Label(image=img_list[number_image - 1])

    back_btn = Button(root, text="<<", command=lambda:event_back(number_image - 1))
    forward_btn = Button(root, text=">>", command=lambda:event_forward(number_image + 1))
    if number_image == 0:
         back_btn = Button(root, text="<<", state=DISABLED)

    my_label.grid(row=0, column=0, columnspan=3)
    back_btn.grid(row=1, column=0)
    forward_btn.grid(row=1, column=2)




back_btn = Button(root, text="<<", command=event_back, state=DISABLED)
quit_btn = Button(root, text="exit", command=root.quit)
forward_btn = Button(root, text=">>", command=lambda:event_forward(2))
my_label = Label(root, image=img1)



my_label.grid(row=0, column=0, columnspan=3)
back_btn.grid(row=1, column=0)
quit_btn.grid(row=1, column=1)
forward_btn.grid(row=1, column=2)
root.mainloop()