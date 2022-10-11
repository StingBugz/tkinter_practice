from tkinter import *
from tkinter import messagebox
from tkinter.font import BOLD
import mysql.connector
import connectdb

root = Tk()
root.title("Sign Up")
icon_app = PhotoImage(file="./source/favicon/user.png")
root.tk.call("wm","iconphoto",root._w, icon_app)
root.geometry("400x600")

def event_submit():
    try:
        field_customer_data = "f_name, l_name, zipcode, email, address_1, address_2, city, state, country, phone, price, payment_method, discount_code"
        data = connectdb.conn(f"""INSERT INTO customer_data({field_customer_data}) VALUES(
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
            '{price_entry.get()}',
            '{payment_method_entry.get()}',
            '{discount_code_entry.get()}'
        )""")
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
        print("insert data success")

    except Exception as e:
        messagebox.showerror("Database", str(e))
        raise Exception("insert data failed") from e
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

#title
lb_title = Label(root, text="Sign Up", font=("helvetica",25,BOLD))
lb_title.grid(row=0, column=0, pady=10,sticky=W+E, columnspan=2)

#frames
frame_input = Frame(root, borderwidth=0, highlightthickness=0)
frame_input.grid(row=1,column=0)

frame_button = Frame(root, borderwidth=0, highlightthickness=0)
frame_button.grid(row=2,column=0, pady=10, padx=30)

#create label for inserting data
f_name_lb = Label(frame_input, text="First Name").grid(row=0,column=0,padx=10, pady=5, sticky=W)
l_name_lb = Label(frame_input, text="Last Name").grid(row=1,column=0,padx=10, pady=5, sticky=W)
zipcode_lb = Label(frame_input, text="Zipcode").grid(row=2,column=0,padx=10, pady=5, sticky=W)
email_lb = Label(frame_input, text="Email").grid(row=3,column=0,padx=10, pady=5, sticky=W)
address1_lb = Label(frame_input,text="Address 1").grid(row=4,column=0,padx=10, pady=5, sticky=W)
address2_lb = Label(frame_input, text="Address 2").grid(row=5,column=0,padx=10, pady=5, sticky=W)
city_lb = Label(frame_input, text="City").grid(row=6,column=0,padx=10, pady=5, sticky=W)
state_lb = Label(frame_input, text="State").grid(row=7,column=0,padx=10, pady=5, sticky=W)
country_lb = Label(frame_input, text="Country").grid(row=8,column=0,padx=10, pady=5, sticky=W)
phone_lb = Label(frame_input, text="Phone Number").grid(row=9,column=0,padx=10, pady=5, sticky=W)
price_lb = Label(frame_input, text="Price").grid(row=10,column=0,padx=10, pady=5, sticky=W)
payment_method_lb = Label(frame_input, text="Payment Method").grid(row=11,column=0,padx=10, pady=5, sticky=W)
discount_code_lb = Label(frame_input, text="Discount Code").grid(row=12,column=0,padx=10, pady=5, sticky=W)

#create entry box for each of those label
f_name_entry = Entry(frame_input)
l_name_entry = Entry(frame_input)
zipcode_entry = Entry(frame_input)
email_entry = Entry(frame_input)
address1_entry = Entry(frame_input)
address2_entry = Entry(frame_input)
city_entry = Entry(frame_input)
state_entry = Entry(frame_input)
country_entry = Entry(frame_input)
phone_entry = Entry(frame_input)
price_entry = Entry(frame_input)
payment_method_entry = Entry(frame_input)
discount_code_entry = Entry(frame_input)

#place on grid
f_name_entry.grid(row=0,column=1,padx=15,pady=5,ipadx=30)
l_name_entry.grid(row=1,column=1,padx=15,pady=5,ipadx=30)
zipcode_entry.grid(row=2,column=1,padx=15,pady=5,ipadx=30)
email_entry.grid(row=3,column=1,padx=15,pady=5,ipadx=30)
address1_entry.grid(row=4,column=1,padx=15,pady=5,ipadx=30)
address2_entry.grid(row=5,column=1,padx=15,pady=5,ipadx=30)
city_entry.grid(row=6,column=1,padx=15,pady=5,ipadx=30)
state_entry.grid(row=7,column=1,padx=15,pady=5,ipadx=30)
country_entry.grid(row=8,column=1,padx=15,pady=5,ipadx=30)
phone_entry.grid(row=9,column=1,padx=15,pady=5,ipadx=30)
price_entry.grid(row=10,column=1,padx=15,pady=5,ipadx=30)
payment_method_entry.grid(row=11,column=1,padx=15,pady=5,ipadx=30)
discount_code_entry.grid(row=12,column=1,padx=15,pady=5,ipadx=30)

#button submit
btn_submit = Button(frame_button, text="Submit", command=event_submit)
btn_clear = Button(frame_button, text="Clear Field", command=event_clear)

#place button on grid
btn_submit.grid(row=0, column=0, padx=10)
btn_clear.grid(row=0, column=1,padx=10)

root.mainloop()
