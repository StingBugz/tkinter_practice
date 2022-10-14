from tkinter import *
from tkinter.font import BOLD

def buku_pesanan(qt:int):
    jenis_up = []
    harga_up = []
    qt_up = []
    all = []
    for i in range(qt):
        bukuPesan = Toplevel()
        bukuPesan.title(f"Buku Pesanan")
        icon_app = PhotoImage(file="./7_gerobak_fried_chicken/favicon/chicken.png")
        bukuPesan.tk.call("wm","iconphoto", bukuPesan._w, icon_app)
        bukuPesan.resizable(0,0)

        def event_tulis_pesan():
            jenis_up.append(jenis.get())
            qt_up.append(qt_entry.get())
            if jenis.get()=="Dada":
                harga_up.append(8000 * int(qt_entry.get())) 
            elif jenis.get()=="Paha":
                harga_up.append(7000 * int(qt_entry.get()))
            elif jenis.get()=="Sayap":
                harga_up.append(5000 * int(qt_entry.get())) 
            else:
                harga_up.append(0 * int(qt_entry.get()))

            bukuPesan.destroy()    
            bukuPesan.quit()


        jenis_list = ["Dada","Paha","Sayap"]
        jenis = StringVar()
        jenis.set(jenis_list[0])

        title_lb = Label(bukuPesan, text=f"Pesanan {i+1}", font=("helvetica", 15, BOLD),padx=10, pady=5)
        title_lb.grid(row=0, column=0)

        jenis_drop = OptionMenu(bukuPesan, jenis, *jenis_list)
        jenis_drop.grid(row=1, column=0, pady=10)

        qt_lb = Label(bukuPesan, text="berapa potong", font=("helvetica", 10,BOLD))
        qt_entry = Entry(bukuPesan, width=10, justify="center")
        qt_lb.grid(row=2, column=0, pady=(10,0))
        qt_entry.grid(row=3, column=0)

        btn_pesan = Button(bukuPesan, text="Pesan", command=event_tulis_pesan)
        btn_pesan.grid(row=4,column=0, pady=5)
        bukuPesan.mainloop()
    all.append(jenis_up)
    all.append(harga_up)
    all.append(qt_up)
    return all

    