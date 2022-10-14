from tkinter import *
from tkinter import messagebox
from tkinter.font import BOLD
import buku_pesanan
import struk

root = Tk()
root.title("Gerobak Fried Chicken")
icon_app = PhotoImage(file="./7_gerobak_fried_chicken/favicon/chicken.png")
root.tk.call("wm","iconphoto", root._w, icon_app)
root.resizable(0,0)
root.eval('tk::PlaceWindow . center')

#function
def event_buat_pesan():
    try:
        global harga_total_pesanan
        global jenis_pesan
        global harga_pesan
        global jumlah_pesan
        harga_total_pesanan = 0
        total_pesan = int(qt_entry.get())
        qt_entry.delete(0,END)
        data = buku_pesanan.buku_pesanan(qt=total_pesan)
        jenis_pesan = data[0]
        harga_pesan = data[1]
        jumlah_pesan = data[2]
        for total in data[1]:
            harga_total_pesanan+=total
    except ValueError:
        messagebox.showwarning("Warning", "please fill out the field with number of your order")
    except Exception as e:
        messagebox.showerror("Error", str(e))
        raise Exception from e
def event_cetak_struk():
    try:
        struk.struk(jenis=jenis_pesan, harga=harga_pesan, total=harga_total_pesanan, qt=jumlah_pesan)
    except Exception as e:
        messagebox.showwarning("Warning", "Data is Empty.\nplease fill the form on buku pesanan first")
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
qt_lbl = Label(frame_btn, text="banyak pesanan", font=("helvetica", 10)) 
qt_entry = Entry(frame_btn, justify="center")
btn_pesan = Button(frame_btn, text="Buat pesanan", command=event_buat_pesan)
btn_struk = Button(frame_btn, text="Cetak Struk", command=event_cetak_struk)
btn_quit = Button(frame_btn, text="Quit", command=event_quit)

qt_lbl.grid(row=0,column=0,sticky=W+E, columnspan=3)
qt_entry.grid(row=1, column=0, sticky=W+E, columnspan=3,padx=10)
btn_pesan.grid(row=2, column=0, padx=5, pady=10)
btn_quit.grid(row=2, column=1, padx=5)
btn_struk.grid(row=2, column=2, padx=5)

root.mainloop()