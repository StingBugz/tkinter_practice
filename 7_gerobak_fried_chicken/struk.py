from tkinter import *
from tkinter import messagebox
from tkinter.font import BOLD

def struk(jenis:list,harga:list,qt:list,total):
    try:
        #biaya admin
        ppn = total * 0.1

        struk = Toplevel()
        struk.title("Struk")
        icon_app = PhotoImage(file="./7_gerobak_fried_chicken/favicon/chicken.png")
        struk.tk.call("wm","iconphoto", struk._w, icon_app)
        struk.resizable(0,0)
        order = 0

        for i in range(len(jenis)):
            frame_data = Frame(struk, padx=10, pady=5, highlightcolor="Black", borderwidth=3, highlightthickness=3)
            lb_urutan = Label(frame_data, text=f"Pesanan {order+1}", font=("helvetica", 15, BOLD))
            lb_jenis = Label(frame_data, text="Jenis", font=("helvetica", 10))
            lb_qt = Label(frame_data, text="QTY", font=("helvetica", 10))
            lb_harga = Label(frame_data, text="Subtotal", font=("helvetica", 10))
            lb_jenis_data = Label(frame_data, text=f"Rp.{jenis[i]}", font=("helvetica", 10))
            lb_qt_data = Label(frame_data, text=f"{qt[i]} potong", font=("helvetica", 10))
            lb_harga_data = Label(frame_data, text=f"Rp.{harga[i]}", font=("helvetica", 10))

            frame_data.grid(row=i,column=0, sticky=W+E)
            lb_urutan.grid(row=0, column=0, columnspan=2, padx=10,sticky=W+E)
            lb_jenis.grid(row=1, column=0,padx=5, sticky=W)
            lb_jenis_data.grid(row=1, column=1, padx=5,sticky=W)
            lb_qt.grid(row=2, column=0, padx=5,sticky=W)
            lb_qt_data.grid(row=2, column=1, padx=5,sticky=W)
            lb_harga.grid(row=3, column=0, padx=5,sticky=W)
            lb_harga_data.grid(row=3, column=1, padx=5,sticky=W)
            order+=1

        frame_final = Frame(struk, padx=10,pady=5, highlightcolor="Black", borderwidth=3, highlightthickness=3)
        frame_final.grid(row=order+1,column=0, sticky=W+E)

        lb_ppn = Label(frame_final, text="Biaya PPN 10%")
        lb_ppn_data = Label(frame_final, text=f"Rp.{ppn}")
        lb_total = Label(frame_final, text="Total")
        lb_total_data = Label(frame_final, text=f"Rp.{total}")
        lb_ppn.grid(row=0,column=0,padx=5, sticky=W)
        lb_ppn_data.grid(row=0, column=1,padx=5 ,sticky=W)
        lb_total.grid(row=1,column=0,padx=5, sticky=W)
        lb_total_data.grid(row=1, column=1,padx=5 ,sticky=W)

        struk.mainloop()
    except Exception as e:
        messagebox.showerror("Error", str(e))
