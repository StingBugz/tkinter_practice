from tkinter import *
from tkinter import messagebox
from xmlrpc.client import ResponseError

root = Tk()
root.title("Message box")
icon = PhotoImage(file="./source/favicon/message.png")
root.tk.call("wm","iconphoto", root._w, icon)
#showinfo, showwarning, showerror, askquestion, askokcancel, askyesno, askretrycancel, askyesnocancel

def event_popup():
    # response = messagebox.showinfo("Popup message", "Hello World!")
    # Label(root,text=response).pack()

    # response = messagebox.showwarning("Popup message", "Hello World!")
    # Label(root,text=response).pack()

    # response = messagebox.showerror("Popup message", "Hello World!")
    # Label(root,text=response).pack()

    # response = messagebox.askquestion("Popup message", "Hello World!")
    # Label(root,text=response).pack()
    # if response == "yes":
    #     Label(root, text="you clicked yes").pack()
    # else:
    #     Label(root, text="you clicked no!").pack()

    # response = messagebox.askokcancel("Popup message", "Hello World!")
    # Label(root,text=response).pack()
    # if response == 1:
    #     Label(root, text="you clicked yes").pack()
    # else:
    #     Label(root, text="you clicked no!").pack()

    # response = messagebox.askyesno("Popup message", "Hello World!")
    # Label(root,text=response).pack()
    # if response == 1:
    #     Label(root, text="you clicked yes").pack()
    # else:
    #     Label(root, text="you clicked no!").pack()

    # response = messagebox.askretrycancel("Popup message", "Hello World!")
    # Label(root,text=response).pack()
    # if response:
    #     Label(root, text="you clicked retry").pack()
    # else:
    #     Label(root, text="you clicked cancel").pack()

    response = messagebox.askyesnocancel("Popup message", "Hello World!")
    Label(root,text=response).pack()
    if response == 1:
        Label(root, text="you clicked yes").pack()
    elif response == 0:
        Label(root, text="you clicked no").pack()
    else:
        Label(root, text="you clicked cancel").pack()


Button(root, text="Popup", command=event_popup).pack()

root.mainloop()