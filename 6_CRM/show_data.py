from tkinter import *
from tkinter import messagebox
from tkinter.font import BOLD, ITALIC
from mysql.connector.errors import ProgrammingError
import csv
import connectdb
import update_window

def show_data(data:list):
    global list_data
    list_data = data
    rootShowData = Toplevel()
    rootShowData.title("Show Data")
    icon_app = PhotoImage(file="./source/favicon/user.png")
    rootShowData.tk.call("wm","iconphoto",rootShowData._w,icon_app)
    rootShowData.resizable(0,0)
    rootShowData.geometry("+50+300")
    # print(data)
    #function
    def event_search():
        try:
            responsedb = connectdb.read(f"""SELECT * FROM customer_data WHERE
                user_id LIKE '%{entry_search.get()}%' OR
                f_name LIKE '%{entry_search.get()}%' OR
                l_name LIKE '%{entry_search.get()}%' OR
                zipcode LIKE '%{entry_search.get()}%' OR
                email LIKE '%{entry_search.get()}%' OR
                address_1 LIKE '%{entry_search.get()}%' OR
                address_2 LIKE '%{entry_search.get()}%' OR
                city LIKE '%{entry_search.get()}%' OR
                state LIKE '%{entry_search.get()}%' OR
                country LIKE '%{entry_search.get()}%' OR
                phone LIKE '%{entry_search.get()}%' OR
                price LIKE '%{entry_search.get()}%' OR
                payment_method LIKE '%{entry_search.get()}%' OR
                discount_code LIKE '%{entry_search.get()}%'
            """)
            show_data(responsedb)
            rootShowData.destroy()
        except Exception as e:
            messagebox.showerror("Error",str(e))
            raise Exception from e
           
    def event_update():
        try:
            responsedb = connectdb.read(f"SELECT * FROM customer_data WHERE user_id={entry_search.get()}")
            update_window.update_window(responsedb)
            rootShowData.destroy()
        except ProgrammingError as e:
            responseErr = messagebox.showerror("Error", "for update please input index of data")
            if responseErr == "ok":
                rootShowData.quit()
        except Exception as err:
            messagebox.showerror("Error",str(err))
            raise Exception from err
            
    def event_delete():
        try:
            connectdb.conn(f"DELETE FROM customer_data WHERE user_id={entry_search.get()}")
            print("delete data success")
        except Exception as e:
            messagebox.showerror("error",str(e))
    
    def event_save_csv(data_list):
        path_csv = "./6_CRM/csv/customer_data.csv"
        with open(path_csv, "w+", newline="") as f:
            w = csv.writer(f, dialect="excel")
            for i in data_list:
                w.writerow(i)
    
    def event_home():
        rootShowData.destroy()
        show_data(list_data)
        

    
    

    #button
    frame_search = Frame(rootShowData)
    frame_search.grid(row=0, column=0,pady=10, sticky=W)
    
    entry_search = Entry(frame_search, width=10)
    entry_search.insert(0, "search...")
    entry_search.config(font=("helvetica", 10, ITALIC))
    entry_search.grid(row=0, column=0, padx=(5,10), ipady=5)

    btn_search = Button(frame_search, text="Search", command=event_search)
    btn_update = Button(frame_search, text="Update", command=event_update)
    btn_delete = Button(frame_search, text="Delete", command=event_delete)
    btn_save_csv = Button(frame_search, text="Save Excel", command=lambda:event_save_csv(data))
    btn_home = Button(frame_search, text="Reset", command=event_home)

    btn_search.grid(row=0, column=1, padx=5, sticky=W)
    btn_update.grid(row=0, column=2, padx=5, sticky=W)
    btn_delete.grid(row=0, column=3, padx=5, sticky=W)
    btn_save_csv.grid(row=0, column=4, padx=5, sticky=W)
    btn_home.grid(row=0,column=5, padx=5, sticky=W)

    #frame data
    frame_data = Frame(rootShowData)
    frame_data.grid(row=1, column=0,pady=(0,10), sticky=W)

    header = ["No","First Name", "Last Name","Zipcode","Email","Address 1","Address 2","City","State","Country","Phone","Price","Payment Method","Discount Code"]
    for i in range(len(header)):
        text_header = Text(frame_data,height=1,width=12,font=("helvetica",9,BOLD), background="#000000", foreground="#ffffff")
        text_header.insert(INSERT, header[i])
        text_header.config(state="disabled")
        text_header.grid(row=0, column=i)

    rowindex = 1
    for i in range(len(data)):
        for j in range(len(header)):
            text_data = Text(frame_data, height=2, width=14, font=("helvetica",8))
            text_data.insert(INSERT,data[i][j])
            text_data.config(state="disabled")
            text_data.grid(row=i + rowindex,column=j)


            
