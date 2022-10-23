from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from tkinter.font import BOLD
import connectdb
import show_data


def update_window(data:list):
    rootUpdate = Toplevel()
    rootUpdate.title("Update Window")
    icon_app = PhotoImage(file="./source/favicon/user.png")
    rootUpdate.tk.call("wm","iconphoto",rootUpdate._w,icon_app)
    rootUpdate.geometry("+50+150")
    #update function
    def event_update(data:list):
        try:
            price = price_entry.get().replace("$","")        
            connectdb.conn(f"""UPDATE customer_data SET
                f_name='{f_name_entry.get()}',
                l_name='{l_name_entry.get()}',
                zipcode='{zipcode_entry.get()}',
                email='{email_entry.get()}',
                address_1='{address1_entry.get()}',
                address_2='{address2_entry.get()}',
                city='{city_entry.get()}',
                state='{state_entry.get()}',
                country='{country_entry.get()}',
                phone='{phone_entry.get()}',
                price='{price}',
                payment_method='{payment_method_combo.get()}',
                discount_code='{discount_code_entry.get()}'
                WHERE user_id='{data[0][0]}'
                """)
            data = connectdb.read(f"SELECT * FROM customer_data")
            show_data.show_data(data)
            rootUpdate.destroy()
            print("update data success")
        except Exception as e:
            messagebox.showerror("Error",str(e))
            raise Exception from e

    for i in data:
        #title
        lb_title = Label(rootUpdate, text=f"Update Data {i[1]}", font=("helvetica",25,BOLD))
        lb_title.grid(row=0, column=0, pady=10,sticky=W+E, columnspan=2)

        #frames
        frame_input = Frame(rootUpdate, borderwidth=0, highlightthickness=0)
        frame_input.grid(row=1,column=0)

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
        f_name_entry.insert(0,i[1])
        l_name_entry = Entry(frame_input)
        l_name_entry.insert(0,i[2])
        zipcode_entry = Entry(frame_input)
        zipcode_entry.insert(0,i[3])
        email_entry = Entry(frame_input)
        email_entry.insert(0,i[4])
        address1_entry = Entry(frame_input)
        address1_entry.insert(0,i[5])
        address2_entry = Entry(frame_input)
        address2_entry.insert(0,i[6])
        city_entry = Entry(frame_input)
        city_entry.insert(0,i[7])
        state_entry = Entry(frame_input)
        state_entry.insert(0,i[8])
        country_entry = Entry(frame_input)
        country_entry.insert(0,i[9])
        phone_entry = Entry(frame_input)
        phone_entry.insert(0,i[10])
        price_entry = Entry(frame_input)
        price_entry.insert(0,f"${i[11]}")
        payment_method_combo = ttk.Combobox(frame_input, values=["credit","cash"], width=26)
        payment_method_combo.set(f"{i[12]}")
        payment_method_combo.config(state="readonly")
        discount_code_entry = Entry(frame_input)
        discount_code_entry.insert(0,i[13])

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
        payment_method_combo.grid(row=11,column=1,padx=15,pady=5)
        discount_code_entry.grid(row=12,column=1,padx=15,pady=5,ipadx=30)

        #frame button
        frame_button = Frame(rootUpdate)
        frame_button.grid(row=2, column=0, sticky=E)

        #button update
        btn_update = Button(frame_button, text="Save", width=10, command=lambda:event_update(data))
        btn_update.grid(row=0,column=0, padx=5, pady=10)
        #button quit
        btn_quit = Button(frame_button, text="Quit", width=10, command=rootUpdate.destroy)
        btn_quit.grid(row=0, column=1, padx=(5,15), pady=10)