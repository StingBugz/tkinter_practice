from tkinter import *
from tkinter import messagebox
from tkinter.font import BOLD


def list_pesanan(dict:dict):
    try:
        showData = Toplevel()
        showData.title("List Pesanan")
        iconapp = PhotoImage(file="./7_gerobak_fried_chicken/favicon/grid.png")
        showData.tk.call("wm","iconphoto", showData._w,iconapp)
        showData.resizable(0,0)

        #fungsi delete data
        def delete_data():
            pass
        #buat refresh data
        def refresh_data():
            list_pesanan()
            showData.destroy(dict)
    #title
        lb_title = Label(showData, text="Data Pesanan", font=("helvetica", 20, BOLD))
        lb_title.grid(row=0,column=0,pady=(10,0),sticky=W+E)

    #header
        list_header = ["No","Nama","Jenis","QTY","Subtotal"]
        frame_header = Frame(showData, borderwidth=1, highlightthickness=0, highlightcolor="#000000")
        frame_header.grid(row=1,column=0, padx=10, pady=10)
        
        for num_header in range(len(list_header)):
            text_header = Text(frame_header,width=20,height=1, background="#000000", foreground="#ffffff", borderwidth=1)
            text_header.insert(INSERT,list_header[num_header])
            text_header.config(state=DISABLED)
            text_header.grid(row=0, column=num_header)
    #body
        body_row = 2
        for index in dict: #row
            name = dict[f"{index}"][0]
            jenis = dict[f"{index}"][1]
            # harga = dict[f"{index}"][2]
            qt_jenis = dict[f"{index}"][3]
            # qt_order = dict[f"{index}"][4]
            subtotal = dict[f"{index}"][5]

            for i in range(len(list_header)):  #column
                #num
                entry_num = Text(frame_header, width=20, height=1)
                entry_num.insert(INSERT,str(index))
                entry_num.config(state=DISABLED)
                entry_num.grid(row=body_row, column=0)
                #nama
                entry_nama = Text(frame_header, width=20, height=1)
                entry_nama.insert(INSERT,str(name))
                entry_nama.config(state=DISABLED)
                entry_nama.grid(row=body_row, column=1)
                #jenis
                entry_jenis = Text(frame_header, width=20, height=1)
                entry_jenis.insert(INSERT,str(f"{jenis}"))
                entry_jenis.config(state=DISABLED)
                entry_jenis.grid(row=body_row, column=2)
                #qty
                entry_qty = Text(frame_header, width=20, height=1)
                entry_qty.insert(INSERT,str(f"{qt_jenis}"))
                entry_qty.config(state=DISABLED)
                entry_qty.grid(row=body_row, column=3)
                #subtotal
                entry_subtotal = Text(frame_header, width=20, height=1)
                entry_subtotal.insert(INSERT,str(subtotal))
                entry_subtotal.config(state=DISABLED)
                entry_subtotal.grid(row=body_row, column=4)
            body_row+=1
            
            #frame button
            frame_btn = Frame(showData, borderwidth=0,highlightthickness=0)
            frame_btn.grid(row=2, column=0, padx=10,pady=5, sticky=W+E)
            btn_delete = Button(frame_btn, text="Reset",command=delete_data)
            btn_refresh = Button(frame_btn, text="Refresh",command=refresh_data)
            btn_delete.grid(row=0,column=0)
            btn_refresh.grid(row=0,column=1)
    
    except Exception as e:
        messagebox.showerror("Error",str(e))
        raise Exception from e
