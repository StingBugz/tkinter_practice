from tkinter import *
import sqlite3
from turtle import st
import connect


root = Tk()
root.title("Datatabes App")
icon = PhotoImage(file="./source/favicon/database.png")
root.tk.call("wm","iconphoto", root._w, icon)

#frame
frame_data = LabelFrame(root, bd=2, relief=SUNKEN)
frame_data.grid(row=10, column=0,columnspan=2, ipadx=70, pady=(0,10))

#event_submit
def event_submit():
    
    connect.conn(f"""
        INSERT INTO customer_data VALUES("{f_name.get()}","{l_name.get()}","{address.get()}","{city.get()}","{state.get()}",{zipcode.get()})
    """)
    f_name.delete(0, END)
    l_name.delete(0, END)
    address.delete(0, END)
    city.delete(0, END)
    state.delete(0, END)
    zipcode.delete(0, END)

#event_read
def event_read():
    global my_label
    records = connect.read("SELECT *, oid FROM customer_data")
    label_record = ''
    for record in records:
        label_record += str(record[0]) + " " +str(record[1]) +"    "+ str(record[6]) +"\n" 
    my_label = Label(frame_data, text=label_record).pack()
    

#event delete
def event_delete():
    connect.conn(f"DELETE FROM customer_data WHERE oid={delete.get()}")
    delete.delete(0, END)
    my_label.destroy()


# create entry box 
f_name = Entry(root, width=38)
f_name.grid(row=0, column=1, padx=10)
l_name = Entry(root, width=38)
l_name.grid(row=1, column=1, padx=10)
address = Entry(root, width=38)
address.grid(row=2, column=1, padx=10)
city = Entry(root, width=38)
city.grid(row=3, column=1, padx=10)
state = Entry(root, width=38)
state.grid(row=4, column=1, padx=10)
zipcode = Entry(root, width=38)
zipcode.grid(row=5, column=1, padx=10)

#delete entry box
delete = Entry(root, width=38)
delete.grid(row=8, column=1, padx=10)

#create label for each entry box
f_name_label = Label(root, text="First Name ")
f_name_label.grid(row=0, column=0, sticky=W, padx=10, pady=2)
l_name_label = Label(root, text="Last Name ")
l_name_label.grid(row=1, column=0, sticky=W, padx=10, pady=2)
address_label = Label(root, text="Address ")
address_label.grid(row=2, column=0, sticky=W, padx=10,pady=2)
city_label = Label(root, text="City ")
city_label.grid(row=3, column=0, sticky=W, padx=10,pady=2)
state_label = Label(root, text="State ")
state_label.grid(row=4, column=0, sticky=W, padx=10,pady=2)
zipcode_label = Label(root, text="Zipcode ")
zipcode_label.grid(row=5, column=0, sticky=W, padx=10,pady=2)

#delete label
delete_label = Label(root, text="Delete ID")
delete_label.grid(row=8, column=0, sticky=W, padx=(10,0))

#create button
btn_submit = Button(root, text="Create Record To Databases", command=event_submit)
btn_submit.grid(row=6, column=0, columnspan=2, padx=10,pady=2,ipadx=80)

#read button
btn_read = Button(root, text="Show Data From DataBase", command=event_read)
btn_read.grid(row=7, column=0, columnspan=2, padx=10,pady=2, ipadx=85)

#delete button
btn_delete = Button(root, text="Delete Record",command=event_delete)
btn_delete.grid(row=9, column=0, columnspan=2, padx=10,pady=(5,10), ipadx=117)

root.mainloop()