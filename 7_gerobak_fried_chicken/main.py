from tkinter import *
from tkinter import messagebox
from tkinter.font import BOLD
import buku_pesanan
import struk
import list_pesanan

root = Tk()
root.title("Gerobak Fried Chicken")
icon_app = PhotoImage(file="./7_gerobak_fried_chicken/favicon/chicken.png")
root.tk.call("wm","iconphoto", root._w, icon_app)
root.resizable(0,0)
root.eval('tk::PlaceWindow . center')

num = 1
all = []
index = {}


#function
def event_buat_pesan():
    global num
    try:
        harga_total_pesanan = 0
        total_pesan = int(qt_entry.get())
        customer_name = str(name_entry.get())
        qt_entry.delete(0,END)
        name_entry.delete(0,END)

        data = buku_pesanan.buku_pesanan(qt=total_pesan, name=customer_name)

        jenis_pesan = data[0]
        harga_pesan = data[1]
        jumlah_pesan = data[2]
        for total in harga_pesan:
            harga_total_pesanan+=total
        all.append(customer_name)
        all.append(jenis_pesan)
        all.append(harga_pesan)
        all.append(jumlah_pesan)
        all.append(total_pesan)
        all.append(harga_total_pesanan)
        
        index[f"{num}"] = []
        index[f"{num}"] = all.copy()
        all.clear()
        # print(index)
        num+=1
    except ValueError:
        messagebox.showerror("Error", "Tolong Masukkan Jumlah Pesanan")
    except Exception as e:
        messagebox.showerror("Error", str(e))
        raise Exception from e
def event_cetak_struk():
    try:
        if index == {}:
            messagebox.showwarning("Warning", "Data Empty")
        else :
            struk.struk(dict=index)
    except Exception as e:
        messagebox.showerror("Error",str(e))
        raise Exception from e

def event_show_data():
    try:
        list_pesanan.list_pesanan(dict=index)
    except Exception as e:
        messagebox.showerror("Error", str(e))
        raise Exception from e

def event_quit():
    root.quit()
    root.destroy()

#title perusahaan
logo = PhotoImage(file="./7_gerobak_fried_chicken/favicon/chicken_logo.png")
logo_lbl = Label(root, image=logo)
title_lbl = Label(root, text="Gerobak Fried Chicken", font=("helvetica", 15, BOLD))
logo_lbl.grid(row=0,column=0, padx=15, pady=5, sticky=W+E)
title_lbl.grid(row=1, column=0,padx=15, pady=5, sticky=W+E)

#frame button
frame_btn = Frame(root, borderwidth=0, highlightthickness=0)
frame_btn.grid(row=2, column=0)

#button
qt_lbl = Label(frame_btn, text="Jumlah Pesanan", font=("helvetica", 10)) 
qt_entry = Entry(frame_btn, justify="center")
name_lbl = Label(frame_btn, text="Nama Customer", font=("helvetica",10))
name_entry = Entry(frame_btn, justify="center")
name_entry.focus_set()
btn_pesan = Button(frame_btn, text="PESAN",width=15,height=2,background="#a00000",foreground="#fff800",activebackground="#fdf25d",activeforeground="#a00000", command=event_buat_pesan)
btn_struk = Button(frame_btn, text="Struk",height=2,background="Green",foreground="White",activebackground="#fdf25d",activeforeground="#a00000",command=event_cetak_struk)
btn_quit = Button(frame_btn, text="Quit",height=2,background="#000000", foreground="#ffffff",activebackground="#fdf25d",activeforeground="#a00000", command=event_quit)

name_lbl.grid(row=0,column=0,sticky=W+E, columnspan=3)
name_entry.grid(row=1, column=0, sticky=W+E, columnspan=3,padx=10)
qt_lbl.grid(row=2,column=0,sticky=W+E, columnspan=3, pady=(10,0))
qt_entry.grid(row=3, column=0, sticky=W+E, columnspan=3,padx=10)
btn_struk.grid(row=4, column=0, padx=5, pady=(10,0))
btn_pesan.grid(row=4, column=1, padx=5, pady=(10,0))
btn_quit.grid(row=4, column=2, padx=5, pady=(10,0))

#btn show data
btn_show = Button(frame_btn, text="Lihat Semua Pesanan",height=2, width=32, background="#1D1CE5",foreground="#fff800",activebackground="#fdf25d",activeforeground="#a00000",command=event_show_data)
btn_show.grid(row=5, column=0, columnspan=3, pady=(0,5))

root.mainloop()