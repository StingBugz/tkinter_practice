from tkinter import *
from tkinter import messagebox
from tkinter.font import BOLD

def money_format(value):
    y = str(value)
    if len(y) <= 3:
        value = y
        return value
    else:
        p = y[-3:]
        q = y[:-3]
        value = money_format(q) + "." +p
        return value


def struk(dict:dict):
    try:
        for index in dict:
            struk = Toplevel()
            struk.title("Struk")
            icon_app = PhotoImage(file="./7_gerobak_fried_chicken/favicon/chicken.png")
            struk.tk.call("wm","iconphoto", struk._w, icon_app)
            struk.resizable(0,0)

            #masukkan ke pdf untuk print (button)
            def event_print():
                try:
                    if dict == {}:
                        messagebox.showerror("error", "Data empty")
                    else:
                        dict[f"{index}"].clear()
                        struk.destroy()
                except Exception as e:
                    messagebox.showerror("error", str(e))
                    raise Exception from e
            
            name = dict[f"{index}"][0]
            jenis = dict[f"{index}"][1]
            harga = dict[f"{index}"][2]
            qt_jenis = dict[f"{index}"][3]
            qt_order = dict[f"{index}"][4]
            subtotal = dict[f"{index}"][5]
            
            # biaya admin
            ppn = subtotal * 0.1
            #total harga
            total_harga = subtotal + ppn

            order = 1
            #frame nama dan jumlah order
            frame_name = Frame(struk)
            frame_name.grid(row=0,column=0, padx=10, pady=10, sticky=W+E)
            lb_name = Label(frame_name, text=f"Customer: {name}", font=("helvetica", 10,BOLD))
            lb_order = Label(frame_name, text=f"Jumlah Order : {qt_order}", font=("helvetica", 10,BOLD))
            lb_name.grid(row=0, column=0)
            lb_order.grid(row=1,column=0)
            
            
            #frame info selain nama
            for i in range(len(jenis)):
                frame_data = Frame(struk, padx=10, pady=5, highlightcolor="black", borderwidth=3, highlightthickness=3)
                lb_urutan = Label(frame_data, text=f"Pesanan {i+1}", font=("helvetica", 15, BOLD))
                lb_jenis = Label(frame_data, text="Jenis", font=("helvetica", 10))
                lb_qt = Label(frame_data, text="QTY", font=("helvetica", 10))
                lb_harga = Label(frame_data, text="Subtotal", font=("helvetica", 10))
                lb_jenis_data = Label(frame_data, text=f"{jenis[i]}", font=("helvetica", 10))
                lb_qt_data = Label(frame_data, text=f"{qt_jenis[i]} potong", font=("helvetica", 10))
                lb_harga_data = Label(frame_data, text=f"Rp.{money_format(int(harga[i]))},-", font=("helvetica", 10))

                frame_data.grid(row=order+1,column=0, sticky=W+E)
                lb_urutan.grid(row=0, column=0, columnspan=2,sticky=W)
                lb_jenis.grid(row=1, column=0,padx=5, sticky=W)
                lb_jenis_data.grid(row=1, column=1, padx=5,sticky=W)
                lb_qt.grid(row=2, column=0, padx=5,sticky=W)
                lb_qt_data.grid(row=2, column=1, padx=5,sticky=W)
                lb_harga.grid(row=3, column=0, padx=5,sticky=W)
                lb_harga_data.grid(row=3, column=1, padx=5,sticky=W)
                order+=1

            #frame 
            frame_final = Frame(struk, padx=10,pady=5, highlightcolor="Black", borderwidth=3, highlightthickness=3)
            frame_final.grid(row=order+1,column=0,pady=(0,15), sticky=W+E)

            lb_ppn = Label(frame_final, text="Biaya PPN 10%")
            lb_ppn_data = Label(frame_final, text=f"Rp.{money_format(int(ppn))},-")
            lb_total = Label(frame_final, text="Total")
            lb_total_data = Label(frame_final, text=f"Rp.{money_format(int(total_harga))},-")
            lb_ppn.grid(row=0,column=0,padx=5, sticky=W)
            lb_ppn_data.grid(row=0, column=1,padx=5 ,sticky=W)
            lb_total.grid(row=1,column=0,padx=5, sticky=W)
            lb_total_data.grid(row=1, column=1,padx=5 ,sticky=W)
            
            btn_print = Button(frame_final, text="Print",background="#a00000",foreground="#ffffff",activebackground="#fdf25d",activeforeground="#a00000",command=event_print)
            btn_print.grid(row=2, column=0,pady=10,sticky=W+E)


    except Exception as e:
        messagebox.showerror("Error", str(e))
        raise Exception from e

