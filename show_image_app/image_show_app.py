from tkinter import *
from PIL import Image, ImageTk

root = Tk()
root.title('Image Show App')
img = PhotoImage(file="/home/yatora/Documents/tkinter_practice_linux/source/favicon/jp_flag.png")
root.tk.call('wm','iconphoto', root._w, img )



img1 = ImageTk.PhotoImage(Image.open("/home/yatora/Documents/tkinter_practice_linux/source/img/cat_meme1.jpg"))
img2 = ImageTk.PhotoImage(Image.open("/home/yatora/Documents/tkinter_practice_linux/source/img/cat_meme2.jpeg"))
img3 = ImageTk.PhotoImage(Image.open("/home/yatora/Documents/tkinter_practice_linux/source/img/cat_meme3.jpg"))
img4 = ImageTk.PhotoImage(Image.open("/home/yatora/Documents/tkinter_practice_linux/source/img/cat_meme4.jpg"))
img5 = ImageTk.PhotoImage(Image.open("/home/yatora/Documents/tkinter_practice_linux/source/img/cat_meme5.jpg"))
img6 = ImageTk.PhotoImage(Image.open("/home/yatora/Documents/tkinter_practice_linux/source/img/cat_smudge.jpg"))

my_img = [img1, img2, img3, img4, img5, img6]


def event_forward(number_image):
    global labelglobal
    global button_forward
    global button_back
    

    labelglobal.grid_forget()
    labelglobal = Label(image=my_img[number_image - 1])
    button_forward = Button(root, text=">>", command=lambda:event_forward(number_image + 1))
    button_back = Button(root, text="<<", command=lambda:event_back(number_image-1))
    if number_image == 5:
        button_forward = Button(root,text=">>", state=DISABLED)

    labelglobal.grid(row=0, column=0, columnspan=3)
    button_back.grid(row=1, column=0)
    button_forward.grid(row=1, column=2)

def event_back(number_image):
    global labelglobal
    global button_forward
    global button_back
    

    labelglobal.grid_forget()
    labelglobal = Label(image=my_img[number_image - 1])
    button_forward = Button(root, text=">>", command=lambda:event_forward(number_image + 1))
    button_back = Button(root, text="<<", command=lambda:event_back(number_image-1))
    if number_image == 0:
        button_back = Button(root,text="<<", state=DISABLED)

    labelglobal.grid(row=0, column=0, columnspan=3)
    button_back.grid(row=1, column=0)
    button_forward.grid(row=1, column=2)

labelglobal = Label(image=img1)

button_back = Button(root, text="<<", command=event_back, state=DISABLED)
button_quit = Button(root, text="Exit Program", command=root.quit)
button_forward = Button(root, text=">>", command=lambda:event_forward(2))

labelglobal.grid(row=0,column=0, columnspan=3, padx=5, pady=5)
button_back.grid(row=1, column=0)
button_quit.grid(row=1, column=1)
button_forward.grid(row=1, column=2)


root.mainloop()

