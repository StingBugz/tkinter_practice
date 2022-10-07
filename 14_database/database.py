from tkinter import *
import sqlite3
import connect
import update_window


root = Tk()
root.title("Datatabes App")
icon = PhotoImage(file="./source/favicon/database.png")
root.tk.call("wm","iconphoto", root._w, icon)

#frame
frame_data = LabelFrame(root, bd=2, relief=SUNKEN)
frame_data.grid(row=13, column=0,columnspan=2, ipadx=70, pady=(0,10))

#event_submit
def event_submit():
    
    try:
        connect.conn(f"""
        INSERT INTO customer_data VALUES("{f_name.get()}","{l_name.get()}","{address.get()}","{city.get()}","{state.get()}",{zipcode.get()})
    """)
        f_name.delete(0, END)
        l_name.delete(0, END)
        address.delete(0, END)
        city.delete(0, END)
        state.delete(0, END)
        zipcode.delete(0, END)
        print("insert data succces")

    except sqlite3.OperationalError as e:
        raise Exception("insert data failed") from e

#event_read
def event_read():
    try:
        records = connect.read("SELECT *, oid FROM customer_data")
        i = 0
        for record in records:    
            label_name = record[0] + " " + record[1]
            label_id = record[6]
            Label(frame_data, text=label_name).grid(row=i, column=0)
            Label(frame_data, text=label_id).grid(row=i, column=1)
            i+=1
                
        print("show data success")

    except sqlite3.OperationalError as e:
        raise Exception("show data failed") from e
 

#event delete
def event_delete():
    try:
        connect.conn(f"DELETE FROM customer_data WHERE oid={select_id_entry.get()}")
        select_id_entry.delete(0, END)
        print("delete succes success")

    except sqlite3.OperationalError as e:
        raise Exception("delete data failed") from e

def event_update():
    records = connect.read(f"SELECT *,oid FROM customer_data WHERE oid={select_id_entry.get()}")
    select_id_entry.delete(0, END)
    data_record = []
    for record in records:
        for i in range(len(record)):
            data_record.append(record[i])

    update_window.update(data=data_record)
    
# create entry box 
f_name = Entry(root,width=38)
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



#create button
btn_submit = Button(root, text="Create Record To Databases", command=event_submit)
btn_submit.grid(row=6, column=0, columnspan=3, padx=10,pady=2,ipadx=80)

#read button
btn_read = Button(root, text="Show Data From DataBase", command=event_read)
btn_read.grid(row=8, column=0, columnspan=3, padx=10,pady=2, ipadx=85)

#delete button
btn_delete = Button(root, text="Delete Record",command=event_delete)
btn_delete.grid(row=9, column=0, columnspan=3, padx=10, pady=2, ipadx=117)

#update button
btn_update = Button(root, text="Update Record", command=event_update)
btn_update.grid(row=10, column=0, columnspan=3, padx=10, pady=2, ipadx=117)

#delete label
delete_label = Label(root, text="Select ID")
delete_label.grid(row=11, column=0, sticky=W, padx=(10,0))

#delete entry box
select_id_entry = Entry(root, width=38)
select_id_entry.grid(row=11, column=1, padx=10)

root.mainloop()