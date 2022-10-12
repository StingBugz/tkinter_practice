from tkinter import *
from tkinter import messagebox
import mysql.connector
import connectdb
import show_data

root = Tk()
root.title("Customer Relation Manager")
icon_root = PhotoImage(file="./source/favicon/customer.png")
root.tk.call("wm","iconphoto", root._w, icon_root)
root.geometry("400x600")

#connect to database
mydb = mysql.connector.connect(
    host ="localhost",
    user="root",
    passwd="tabelperiodik118",
    database="test"
)
#create database
my_cursor = mydb.cursor()


#functions
def event_submit():
    try:
        connectdb.conn(f"""INSERT INTO customer_data (f_name, l_name, zipcode, email, address_1, address_2, city, state, country, phone, price, payment_method, discount_code)VALUES(
                '{f_name_entry.get()}',
                '{l_name_entry.get()}',
                {zipcode_entry.get()},
                '{email_entry.get()}',
                '{address1_entry.get()}',
                '{address2_entry.get()}',
                '{city_entry.get()}',
                '{state_entry.get()}',
                '{country_entry.get()}',
                '{phone_entry.get()}',
                {price_entry.get()},
                '{payment_method_entry.get()}',
                '{discount_code_entry.get()}')
            """)

        event_clear()
        print("insert data success")
    except Exception as e:
        messagebox.showerror("Database Insert", str(e))
        

def event_show_data():
    response_db = connectdb.read("SELECT * FROM customer_data")
    show_data.show_data_window(data=response_db)

    
def event_clear():
    f_name_entry.delete(0,END)
    l_name_entry.delete(0,END)
    zipcode_entry.delete(0,END)
    email_entry.delete(0,END)
    address1_entry.delete(0,END)
    address2_entry.delete(0,END)
    city_entry.delete(0,END)
    state_entry.delete(0,END)
    country_entry.delete(0,END)
    phone_entry.delete(0,END)
    price_entry.delete(0,END)
    payment_method_entry.delete(0,END)
    discount_code_entry.delete(0,END)

#check table
my_cursor.execute("SELECT * FROM customer_data")
for data in my_cursor.description:
    print(data)



#create label title program
lb_title = Label(root,text="Sign Up Account", font=("Verdana", 20))
lb_title.grid(row=0,column=0, columnspan=2, pady=10,padx=(10,0))

#create label untuk tiap colum database
f_name_label = Label(root,text="First Name", font=("verdana", 10)).grid(row=1, column=0, sticky=W, padx=10, pady=2)
l_name_label = Label(root,text="Last Name", font=("verdana", 10)).grid(row=2, column=0, sticky=W, padx=10,pady=2)
zipcode_label = Label(root,text="Zipcode", font=("verdana", 10)).grid(row=3, column=0, sticky=W, padx=10, pady=2)
email_label = Label(root,text="Email", font=("verdana", 10)).grid(row=4, column=0, sticky=W, padx=10, pady=2)
address1_label = Label(root,text="Address 1", font=("verdana", 10)).grid(row=5, column=0, sticky=W, padx=10, pady=2)
address2_label = Label(root,text="Address 2", font=("verdana", 10)).grid(row=6, column=0, sticky=W, padx=10, pady=2)
city_label = Label(root,text="City", font=("verdana", 10)).grid(row=7, column=0, sticky=W, padx=10, pady=2)
state_label = Label(root,text="State", font=("verdana", 10)).grid(row=8, column=0,sticky=W, padx=10, pady=2)
country_label = Label(root,text="Country", font=("verdana", 10)).grid(row=9, column=0, sticky=W, padx=10, pady=2)
phone_label = Label(root,text="Phone", font=("verdana", 10)).grid(row=10, column=0, sticky=W, padx=10, pady=2)
price_label = Label(root,text="Price", font=("verdana", 10)).grid(row=11, column=0, sticky=W, padx=10, pady=2)
payment_method_label = Label(root,text="Payment Method",font=("verdana", 10)).grid(row=12, column=0, sticky=W, padx=10, pady=2)
discount_code_label = Label(root,text="Discount Code", font=("verdana", 10)).grid(row=13, column=0, sticky=W, padx=10, pady=2)

#create entry box for each data
f_name_entry = Entry(root)
l_name_entry = Entry(root)
zipcode_entry = Entry(root)
email_entry = Entry(root)
address1_entry = Entry(root)
address2_entry = Entry(root)
city_entry = Entry(root)
state_entry = Entry(root)
country_entry = Entry(root)
phone_entry = Entry(root)
price_entry = Entry(root)
payment_method_entry = Entry(root)
discount_code_entry = Entry(root)

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
payment_method_entry.grid(row=12,column=1,ipadx=50)
discount_code_entry.grid(row=13,column=1,ipadx=50)

frame_btn = Frame(root,border=0, borderwidth=0, highlightthickness=0)
frame_btn.grid(row=14, column=0, columnspan=2, sticky=E)
#button submit
btn_submit = Button(frame_btn, text="Submit", width=15,command=event_submit)
btn_submit.grid(row=0, column=0,pady=15, padx=5)
#button clear
btn_clear = Button(frame_btn, text="Clear Fields",width=15, command=event_clear)
btn_clear.grid(row=0, column=1,pady=15, padx=5)
#button show data
btn_show_data = Button(frame_btn, text="Show Data",width=15, command=event_show_data)
btn_show_data.grid(row=1, column=0, pady=10, padx=5)


#print use to check connection to database
print(mydb)
root.mainloop()