from tkinter import *
import sqlite3
import connect
import update_window

root = Tk()
root.title("CRUD App")
icon = PhotoImage(file="./source/favicon/paper.png")
root.tk.call("wm", "iconphoto", root._w, icon)
root.geometry("400x600")

#event read
def event_read():
    try:
        records = connect.read(f"""
                    SELECT *, oid FROM data_mahasiswa
                """)

        for i in range(len(records)):
            full_name = records[i][0] + " " + records[i][1]
            id_mahasiswa = records[i][6]
            label_name = Label(frame_data, text=full_name)
            label_id = Label(frame_data, text=id_mahasiswa)
            label_name.grid(row=i, column=0, padx=(10,0))
            label_id.grid(row=i, column=1, padx=(10,0))
        print("berhasil show data")

    except sqlite3.OperationalError as e:
        raise Exception("show data gagal") from e

#event_create
def event_create():
    try:
        connect.conn(f"""
        INSERT INTO data_mahasiswa VALUES(
            '{f_name_entry.get()}',
            '{l_name_entry.get()}',
            '{address_entry.get()}',
            '{city_entry.get()}',
            '{state_entry.get()}',
            {zipcode_entry.get()}
            )
        """)
        print("berhasil create data")

        f_name_entry.delete(0, END)
        l_name_entry.delete(0, END)
        address_entry.delete(0, END)
        city_entry.delete(0, END)
        state_entry.delete(0, END)
        zipcode_entry.delete(0, END)

    except sqlite3.OperationalError as e:
        raise Exception("insert data gagal") from e

#event_delete
def event_delete():
    try:
        connect.conn(f"""
        DELETE FROM data_mahasiswa WHERE oid={select_id_entry.get()}
        """)
        select_id_entry.delete(0, END)
        
        print("berhasil delete data")

    except sqlite3.OperationalError as e:
        raise Exception("delete data gagal") from e

#event_update
def event_update():
    records = connect.read(f"SELECT *, oid FROM data_mahasiswa WHERE oid={select_id_entry.get()}")

    data_record = []
    for record in records:
        for i in range(len(record)):
            data_record.append(record[i])
    move = update_window.update_data(data_record)
    select_id_entry.delete(0, END)


#create label data
f_name_label = Label(root, text="First Name")
l_name_label = Label(root, text="Last Name")
address_label = Label(root, text="Address")
city_label = Label(root, text="City")
state_label = Label(root, text="State")
zipcode_label = Label(root, text="Zipcode")

#grid label data
f_name_label.grid(row=0, column=0, sticky=W, padx=(5,0), pady=(5,0))
l_name_label.grid(row=1, column=0, sticky=W, padx=(5,0), pady=(5,0))
address_label.grid(row=2, column=0, sticky=W, padx=(5,0), pady=(5,0))
city_label.grid(row=3, column=0, sticky=W, padx=(5,0), pady=(5,0))
state_label.grid(row=4, column=0, sticky=W, padx=(5,0), pady=(5,0))
zipcode_label.grid(row=5, column=0, sticky=W, padx=(5,0), pady=(5,0))

#create entry box
f_name_entry = Entry(root)
l_name_entry = Entry(root)
address_entry = Entry(root)
city_entry = Entry(root)
state_entry = Entry(root)
zipcode_entry = Entry(root)

#grid entry box
f_name_entry.grid(row=0, column=1, padx=(5,0), pady=(5,0), ipadx=60)
l_name_entry.grid(row=1, column=1, padx=(5,0), pady=(5,0), ipadx=60)
address_entry.grid(row=2, column=1, padx=(5,0), pady=(5,0), ipadx=60)
city_entry.grid(row=3, column=1, padx=(5,0), pady=(5,0), ipadx=60)
state_entry.grid(row=4, column=1, padx=(5,0), pady=(5,0), ipadx=60)
zipcode_entry.grid(row=5, column=1, padx=(5,0), pady=(5,0), ipadx=60)

#button read
btn_read = Button(root, text="Show Data", command=event_read)
btn_read.grid(row=6, column=0, columnspan=2, padx=(80,0),pady=(10, 0), ipadx=50)

#button create
btn_create = Button(root, text="Create Data", command=event_create)
btn_create.grid(row=7, column=0, columnspan=2, padx=(80,0),pady=(10, 0), ipadx=45)


#button delete
btn_delete = Button(root, text="Delete Data", command=event_delete)
btn_delete.grid(row=8, column=0, columnspan=2, padx=(80,0),pady=(10, 0), ipadx=45)

#button update
btn_update = Button(root, text="Update Data", command=event_update)
btn_update.grid(row=9, column=0, columnspan=2, padx=(80,0),pady=(10, 0), ipadx=43)

#SELECT ID
select_id_label = Label(root, text="Select ID")
select_id_label.grid(row=10, column=0, sticky=W, padx=(5,0), pady=(5,0))

select_id_entry = Entry(root)
select_id_entry.grid(row=10, column=1, padx=(5,0), pady=(5,0), ipadx=60)


#frame show data
frame_data = LabelFrame(root, padx=50)
frame_data.grid(row=11, column=1, padx=(5, 0), pady=(10, 0), ipady=70)


root.mainloop()