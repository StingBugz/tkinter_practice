from tkinter import * 

root = Tk()

def eventClick():
    hello = text.get()
    label1 = Label(root,text="hello " + hello, padx="20px",pady="10px")
    label1.pack()    

text = Entry(root,width=50)
text.pack()
text.insert(0, "name : ")

button1 = Button(root,text="Click", pady=10, padx=20, command=eventClick)
button1.pack()
root.mainloop()