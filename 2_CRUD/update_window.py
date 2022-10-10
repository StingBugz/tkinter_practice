from tkinter import *
import sqlite3
from tkinter import messagebox
import connect


def update_data(data):
    if data == []:
        response = messagebox.showerror("Error", "Data Tidak ada, untuk menampilkan data klik Show Data")
    else:
        edit = Toplevel()
        edit.title("Update Data " + data[0])
        icon = PhotoImage(file="./source/favicon/paper.png")
        edit.tk.call("wm","iconphoto", edit._w, icon)
        edit.geometry("400x400")
        
        def event_save():
            try:
                connect.conn(f"""
                UPDATE data_mahasiswa 
                SET f_name = '{f_name_entry.get()}',
                    l_name = '{l_name_entry.get()}',
                    address = '{address_entry.get()}',
                    city = '{city_entry.get()}',
                    state = '{state_entry.get()}',
                    zipcode = {zipcode_entry.get()}
                WHERE oid = {data[6]}
                 """)
                print("berhasil update data")
                edit.destroy()
            except sqlite3.OperationalError as e:
                raise Exception("gagal update data") from e
            

        #create label data
        f_name_label = Label(edit, text="First Name")
        l_name_label = Label(edit, text="Last Name")
        address_label = Label(edit, text="Address")
        city_label = Label(edit, text="City")
        state_label = Label(edit, text="State")
        zipcode_label = Label(edit, text="Zipcode")

        #grid label data
        f_name_label.grid(row=0, column=0, sticky=W, padx=(5,0), pady=(5,0))
        l_name_label.grid(row=1, column=0, sticky=W, padx=(5,0), pady=(5,0))
        address_label.grid(row=2, column=0, sticky=W, padx=(5,0), pady=(5,0))
        city_label.grid(row=3, column=0, sticky=W, padx=(5,0), pady=(5,0))
        state_label.grid(row=4, column=0, sticky=W, padx=(5,0), pady=(5,0))
        zipcode_label.grid(row=5, column=0, sticky=W, padx=(5,0), pady=(5,0))

        #create entry box
        f_name_entry = Entry(edit)
        f_name_entry.insert(0,str(data[0]))
        l_name_entry = Entry(edit)
        l_name_entry.insert(0,str(data[1]))
        address_entry = Entry(edit)
        address_entry.insert(0,str(data[2]))
        city_entry = Entry(edit)
        city_entry.insert(0,str(data[3]))
        state_entry = Entry(edit)
        state_entry.insert(0,str(data[4]))
        zipcode_entry = Entry(edit)
        zipcode_entry.insert(0,str(data[5]))

        #grid entry box
        f_name_entry.grid(row=0, column=1, padx=(5,0), pady=(5,0), ipadx=60)
        l_name_entry.grid(row=1, column=1, padx=(5,0), pady=(5,0), ipadx=60)
        address_entry.grid(row=2, column=1, padx=(5,0), pady=(5,0), ipadx=60)
        city_entry.grid(row=3, column=1, padx=(5,0), pady=(5,0), ipadx=60)
        state_entry.grid(row=4, column=1, padx=(5,0), pady=(5,0), ipadx=60)
        zipcode_entry.grid(row=5, column=1, padx=(5,0), pady=(5,0), ipadx=60)

        btn_save = Button(edit, text="Save Data", command=event_save)
        btn_save.grid(row=6, column=0, columnspan=2, padx=(80,0),pady=(10, 0), ipadx=50)

        edit.mainloop()
