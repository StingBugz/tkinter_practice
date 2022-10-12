from tkinter import *
from tkinter.font import BOLD
import csv


def show_data_window(data:list):
    rootShowData = Toplevel()
    rootShowData.title("Show Database")
    icon_app = PhotoImage(file="./source/favicon/customer.png")
    rootShowData.tk.call("wm","iconphoto", rootShowData._w, icon_app)
    rootShowData.geometry("1380x500")

    def event_save_csv(data_list):
        with open('customer.csv','a', newline="") as f:
            c = csv.writer(f, dialect="excel")
            for i in data_list:
                c.writerow(i)
    #title
    title_label = Label(rootShowData, text="DATA LIST", font=("verdana", 15, BOLD))
    title_label.grid(row=0, column=0, sticky=W+E)

    #frame for table data list
    frame_list_data = Frame(rootShowData)
    frame_list_data.grid(row=1,column=0, padx=10, pady=10)

    #make header
    header = ["First Name", "Last Name", "Zipcode", "Email", "Address 1", "Address 2", "City", "State", "Country", "Phone", "Price", "Payment", "Referal"]
    x=0 #looping1
    y=1 #looping2
    for i in header: #row0
        entry_data_list_header = Entry(frame_list_data,font=("verdana", 8, BOLD),width=10,bg='Black',fg='White')
        entry_data_list_header.insert(0,i)
        entry_data_list_header.grid(row=0,column=x,sticky=W+E)
        x+=1
    #data_list
    data_list = []
    for j in range(len(data)):
        c_data = list(data[j])
        data_list.append(c_data)
        c_data.remove(c_data[-1])
        for k in range(len(c_data)):    
            entry_data_list = Entry(frame_list_data,font=("verdana",6))
            entry_data_list.insert(0,c_data[k])
            entry_data_list.grid(row=j+y, column=k)
    
    
    #button save
    btn_save = Button(rootShowData, text="save to CVS", command=lambda:event_save_csv(data_list))
    btn_save.grid(row=3,column=0, padx=10, sticky=W)
    rootShowData.mainloop()