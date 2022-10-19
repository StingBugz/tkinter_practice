from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from tkinter.font import BOLD, ITALIC
import csv
from turtle import width
import connectdb


def show_data_window(data:list):
    rootShowData = Toplevel()
    rootShowData.title("Show Database")
    icon_app = PhotoImage(file="./source/favicon/customer.png")
    rootShowData.tk.call("wm","iconphoto", rootShowData._w, icon_app)
    rootShowData.resizable(0,0)


    def event_save_csv(data_list):
        with open('D:/Python/17_crm/csv/customer.csv','w+', newline="") as f:
            # f.truncate()
            c = csv.writer(f, dialect="excel")
            for i in data_list:
                c.writerow(i)
   
    def event_update(id_list):
        id = entry_id.get()
        ",".join(id_list)
        if id in id_list:
            update = Toplevel()
            update.title("Update Data")
            update.geometry("400x500")
            update.resizable(0,0)
            rootShowData.iconify()
            responsedb = connectdb.read(f"SELECT * FROM customer_data WHERE user_id='{id}'")
            # print(responsedb)
            Label(update, text=f"Update Data {responsedb[0][1]}", font=("helvetica",15,BOLD)).grid(row=0,column=0,columnspan=2)
            
            #create label untuk tiap colum database
            Label(update,text="First Name", font=("verdana", 10)).grid(row=1, column=0, sticky=W, padx=10, pady=2)
            Label(update,text="Last Name", font=("verdana", 10)).grid(row=2, column=0, sticky=W, padx=10,pady=2)
            Label(update,text="Zipcode", font=("verdana", 10)).grid(row=3, column=0, sticky=W, padx=10, pady=2)
            Label(update,text="Email", font=("verdana", 10)).grid(row=4, column=0, sticky=W, padx=10, pady=2)
            Label(update,text="Address 1", font=("verdana", 10)).grid(row=5, column=0, sticky=W, padx=10, pady=2)
            Label(update,text="Address 2", font=("verdana", 10)).grid(row=6, column=0, sticky=W, padx=10, pady=2)
            Label(update,text="City", font=("verdana", 10)).grid(row=7, column=0, sticky=W, padx=10, pady=2)
            Label(update,text="State", font=("verdana", 10)).grid(row=8, column=0,sticky=W, padx=10, pady=2)
            Label(update,text="Country", font=("verdana", 10)).grid(row=9, column=0, sticky=W, padx=10, pady=2)
            Label(update,text="Phone", font=("verdana", 10)).grid(row=10, column=0, sticky=W, padx=10, pady=2)
            Label(update,text="Price", font=("verdana", 10)).grid(row=11, column=0, sticky=W, padx=10, pady=2)
            Label(update,text="Payment Method",font=("verdana", 10)).grid(row=12, column=0, sticky=W, padx=10, pady=2)
            Label(update,text="Discount Code", font=("verdana", 10)).grid(row=13, column=0, sticky=W, padx=10, pady=2)

            
            #create entry box for each data
            f_name_entry = Entry(update)
            f_name_entry.insert(0,responsedb[0][1])
            l_name_entry = Entry(update)
            l_name_entry.insert(0,responsedb[0][2])
            zipcode_entry = Entry(update)
            zipcode_entry.insert(0,responsedb[0][3])
            email_entry = Entry(update)
            email_entry.insert(0,responsedb[0][4])
            address1_entry = Entry(update)
            address1_entry.insert(0,responsedb[0][5])
            address2_entry = Entry(update)
            address2_entry.insert(0,responsedb[0][6])
            city_entry = Entry(update)
            city_entry.insert(0,responsedb[0][7])
            state_entry = Entry(update)
            state_entry.insert(0,responsedb[0][8])
            country_entry = Entry(update)
            country_entry.insert(0,responsedb[0][9])
            phone_entry = Entry(update)
            phone_entry.insert(0,responsedb[0][10])
            price_entry = Entry(update)
            price_entry.insert(0,responsedb[0][11])
            payment_method_option = ttk.Combobox(update, values=['credit', 'cash'], state="readonly")
            payment_method_option.set(responsedb[0][12])
            discount_code_entry = Entry(update)
            discount_code_entry.insert(0,responsedb[0][13])

            #place on grid those entry box
            f_name_entry.grid(row=1, column=1,ipadx=50)
            l_name_entry.grid(row=2,column=1,ipadx=50)
            zipcode_entry.grid(row=3,column=1,ipadx=50)
            email_entry.grid(row=4,column=1,ipadx=50)
            address1_entry.grid(row=5,column=1,ipadx=50)
            address2_entry.grid(row=6,column=1,ipadx=50)
            city_entry.grid(row=7,column=1,ipadx=50)
            state_entry.grid(row=8,column=1,ipadx=50)
            country_entry.grid(row=9,column=1,ipadx=50)
            phone_entry.grid(row=10,column=1,ipadx=50)
            price_entry.grid(row=11,column=1,ipadx=50)
            payment_method_option.grid(row=12,column=1,ipadx=30, sticky=W)
            discount_code_entry.grid(row=13,column=1,ipadx=50)
            
            #event_save
            def event_save(user_id):
                try:
                    connectdb.conn(f"""UPDATE customer_data SET 
                        f_name='{f_name_entry.get()}',
                        l_name='{l_name_entry.get()}',
                        zipcode={zipcode_entry.get()},
                        email='{email_entry.get()}',
                        address_1='{address1_entry.get()}',
                        address_2='{address2_entry.get()}',
                        city='{city_entry.get()}',
                        state='{state_entry.get()}',
                        country='{country_entry.get()}',
                        phone='{phone_entry.get()}',
                        price={price_entry.get()},
                        payment_method='{payment_method_option.get()}',
                        discount_code='{discount_code_entry.get()}'

                        WHERE user_id='{user_id}'
                    """)
                    update.destroy()
                    rootShowData.destroy()
                    new_data = connectdb.read("SELECT * FROM customer_data")
                    show_data_window(data=new_data)
                    print("update data success")
                except Exception as e:
                    raise Exception from e
            #event quit
            def event_quit():
                update.destroy()
                rootShowData.destroy()
            #btnsave
            btn_save = Button(update, text="Save",width=10, command=lambda:event_save(id))
            btn_save.grid(row=14,column=0, pady=10,sticky=E)
            #btnquit
            btn_quit = Button(update, text="Quit", width=10,command=event_quit)
            btn_quit.grid(row=14,column=1, pady=10, sticky=E)
        else:
            messagebox.showerror("DatabaseError", "Search Using User ID.")
    
    #event delete
    def event_delete():
        try:
            connectdb.conn(f"DELETE FROM customer_data WHERE user_id={entry_id.get()}")
            rootShowData.destroy()
            new_data = connectdb.read("SELECT * FROM customer_data")
            show_data_window(data=new_data)
            print("delete data success")
        except Exception as e:
            raise Exception from e
    
    #event search
    def event_search():
        try:
            responsedb = connectdb.read(f"""SELECT * FROM customer_data WHERE 
                user_id ='{entry_id.get()}' OR 
                f_name LIKE '%{entry_id.get()}%' OR 
                l_name LIKE '%{entry_id.get()}%' OR 
                zipcode LIKE '%{entry_id.get()}%' OR 
                address_1 LIKE '%{entry_id.get()}%' OR 
                address_2 LIKE '%{entry_id.get()}%' OR 
                city LIKE '%{entry_id.get()}%' OR 
                state LIKE '%{entry_id.get()}%' OR 
                country LIKE '%{entry_id.get()}%' OR 
                price LIKE '%{entry_id.get()}%' OR 
                payment_method LIKE '%{entry_id.get()}%' OR 
                discount_code LIKE '%{entry_id.get()}%'
            """)
            rootShowData.destroy()
            show_data_window(data=responsedb)
        except Exception as e:
            raise Exception from e


    #frame for table data list
    frame_list_data = Frame(rootShowData)
    frame_list_data.grid(row=1,column=0, padx=10, pady=10, columnspan=3)
    #make header
    header = ["ID","First Name", "Last Name", "Zipcode", "Email", "Address 1", "Address 2", "City", "State", "Country", "Phone", "Price", "Payment", "Referal"]
    x=0 #looping1
    y=1 #looping2
    for i in header: #row0
        entry_data_list_header = Text(frame_list_data,font=("verdana", 8, BOLD),width=10, height=1,bg='Black',fg='White')
        entry_data_list_header.insert(INSERT,i)
        entry_data_list_header.config(state="disabled")
        entry_data_list_header.grid(row=0,column=x,sticky=W+E)
        x+=1
    #data_list
    data_list = []
    id_list = []
    for j in range(len(data)):
        c_data = list(data[j])
        data_list.append(c_data)
        id_list.append(str(data_list[j][0]))
        for k in range(len(c_data)):    
            entry_data_list = Text(frame_list_data,font=("verdana",10), width=10,height=2, borderwidth=0, highlightthickness=1)
            entry_data_list.insert(INSERT,c_data[k])
            entry_data_list.config(state="disabled")
            entry_data_list.grid(row=j+y, column=k)
    

    frame_update = Frame(rootShowData, borderwidth=0,highlightthickness=0)
    frame_update.grid(row=0,column=0, padx=10,pady=(10,0),sticky=W)
    #entry id
    entry_id = Entry(frame_update,width=10, justify="left")
    entry_id.insert(0,"search...")
    entry_id.config(font=("helvetica", 8, ITALIC))
    entry_id.grid(row=0,column=0,padx=5,ipady=2,sticky=W)
    #btn_search
    btn_search = Button(frame_update, text="Search", command=event_search)
    btn_search.grid(row=0,column=1,padx=3,sticky=W)
    #btn_update
    btn_update = Button(frame_update, text="Update", command=lambda:event_update(id_list))
    btn_update.grid(row=0, column=2, padx=3,sticky=W)
    #btn_delete
    btn_delete = Button(frame_update, text="Delete", command=event_delete)
    btn_delete.grid(row=0, column=3, padx=3,sticky=W)
    #button save csv
    btn_save_csv = Button(frame_update, text="save to CSV", command=lambda:event_save_csv(data_list))
    btn_save_csv.grid(row=0,column=4, padx=3, sticky=W)