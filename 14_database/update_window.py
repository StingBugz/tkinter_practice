import sqlite3
from tkinter import *
import connect

def update(data:list):
    root_update = Toplevel()
    root_update.title("Update Data " + str(data[0]))
    icon_update = PhotoImage(file="./source/favicon/database.png")
    root_update.tk.call("wm","iconphoto", root_update._w, icon_update)
    root_update.geometry("400x400")

    def event_save():
        try:
            connect.conn(f"""
                UPDATE customer_data 
                SET f_name = '{f_name.get()}',
                    l_name = '{l_name.get()}',
                    address = '{address.get()}',
                    city = '{city.get()}',
                    state = '{state.get()}',
                    zipcode = {zipcode.get()}
                WHERE oid = {data[6]}
            """)
            print("update data success")
            root_update.destroy()
        except sqlite3.OperationalError as e:
            raise Exception("update data failed") from e

    frame_edit = LabelFrame(root_update, pady=10, padx=10)
    frame_edit.grid(row=0, column=0, padx=(20,0), pady=10)
    
    #create label for each entry box
    f_name_label = Label(frame_edit, text="First Name ")
    f_name_label.grid(row=0, column=0, sticky=W, padx=10, pady=2)
    l_name_label = Label(frame_edit, text="Last Name ")
    l_name_label.grid(row=1, column=0, sticky=W, padx=10, pady=2)
    address_label = Label(frame_edit, text="Address ")
    address_label.grid(row=2, column=0, sticky=W, padx=10,pady=2)
    city_label = Label(frame_edit, text="City ")
    city_label.grid(row=3, column=0, sticky=W, padx=10,pady=2)
    state_label = Label(frame_edit, text="State ")
    state_label.grid(row=4, column=0, sticky=W, padx=10,pady=2)
    zipcode_label = Label(frame_edit, text="Zipcode ")
    zipcode_label.grid(row=5, column=0, sticky=W, padx=10,pady=2)

    # create entry box 
    f_name = Entry(frame_edit,width=38)
    f_name.insert(0, data[0])
    f_name.grid(row=0, column=1, padx=10)
    l_name = Entry(frame_edit, width=38)
    l_name.insert(0, data[1])
    l_name.grid(row=1, column=1, padx=10)
    address = Entry(frame_edit, width=38)
    address.insert(0, data[2])
    address.grid(row=2, column=1, padx=10)
    city = Entry(frame_edit, width=38)
    city.insert(0, data[3])
    city.grid(row=3, column=1, padx=10)
    state = Entry(frame_edit, width=38)
    state.insert(0, data[4])
    state.grid(row=4, column=1, padx=10)
    zipcode = Entry(frame_edit, width=38)
    zipcode.insert(0, data[5])
    zipcode.grid(row=5, column=1, padx=10)

    btn_save = Button(root_update, text="Save", command=event_save)
    btn_save.grid(row=1, column=0, padx=10, pady=2, ipadx=125)

    root_update.mainloop()