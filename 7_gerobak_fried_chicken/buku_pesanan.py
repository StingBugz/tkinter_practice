from tkinter import *
from tkinter.font import BOLD
from tkinter import ttk

def buku_pesanan(qt:int, name:str):
    jenis_up = []
    harga_up = []
    qt_up = []
    all = []
    for i in range(qt):
        bukuPesan = Toplevel()
        bukuPesan.title(f"Order")
        icon_app = PhotoImage(file="./7_gerobak_fried_chicken/favicon/chicken.png")
        bukuPesan.tk.call("wm","iconphoto", bukuPesan._w, icon_app)
        bukuPesan.resizable(0,0) 

        def event_tulis_pesan():
            jenis_up.append(jenis_drop.get())
            qt_up.append(qt_entry.get())
            if jenis_drop.get()=="Dada":
                harga_up.append(8000 * int(qt_entry.get())) 
            elif jenis_drop.get()=="Paha":
                harga_up.append(7000 * int(qt_entry.get()))
            elif jenis_drop.get()=="Sayap":
                harga_up.append(5000 * int(qt_entry.get())) 
            else:
                harga_up.append(0 * int(qt_entry.get()))

            bukuPesan.quit()
            bukuPesan.destroy()   
        
        jenis = ["Dada","Paha","Sayap"]

        title_lb = Label(bukuPesan, text=f"Pesanan {i+1}", font=("helvetica", 20, BOLD))
        title_lb.grid(row=0, column=0, padx=35, pady=(10,0))
        lb_name = Label(bukuPesan, text=f"Customer: {name}",font=("helvetica", 10))
        lb_name.grid(row=1,column=0, sticky=W+E)

        lb_jenis_drop = Label(bukuPesan, text="Bagian Ayam", font=("helvetica",12, BOLD))
        lb_jenis_drop.grid(row=2, column=0, pady=(15,0))
        jenis_drop = ttk.Combobox(bukuPesan, values=jenis, state="readonly")
        jenis_drop.set("Dada")
        jenis_drop.grid(row=3, column=0, ipadx=10, padx=5)

        qt_lb = Label(bukuPesan, text="Jumlah Potong", font=("helvetica", 12,BOLD))
        qt_entry = Entry(bukuPesan, width=8, justify="center")
        qt_entry.focus_set()
        qt_lb.grid(row=4, column=0, pady=(10,0))
        qt_entry.grid(row=5, column=0)

        btn_pesan = Button(bukuPesan, text="Pesan",width=10,background="#a00000",foreground="#ffffff",activebackground="#fdf25d",activeforeground="#a00000", command=event_tulis_pesan)
        btn_pesan.grid(row=6,column=0, pady=5)
        bukuPesan.mainloop()

    all.append(jenis_up)
    all.append(harga_up)
    all.append(qt_up)
    return all
#bisa di tambah menu minuman tapi list nya dipisah
    