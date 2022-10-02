from tkinter import *

root =  Tk()
root.title("Dropdown App")
root.geometry("400x400")

options = [
    "日曜日",
    "月曜日",
    "火曜日",
    "水曜日",
    "木曜日",
    "金曜日",
    "土曜日"
]

resolution = [
    "200x200",
    "400x400",
    "600x600",
    "800x800",
    "1000x1000"
]

def event_select():
    day = Label(frame, text=click_day.get())
    res = Label(frame, text=click_res.get())
    root.geometry(click_res.get())
    day.grid(row=2, column=0)
    res.grid(row=2, column=1)

click_day = StringVar()
click_res = StringVar()
click_day.set("日曜日")
click_res.set("400x400")

frame = Frame(root, padx=10, pady=10, bd=2, relief=SUNKEN)
dropdown_day = OptionMenu(frame, click_day, *options)
dropdown_res = OptionMenu(frame, click_res, *resolution)
btn_select = Button(frame, text="Select", command=event_select)
btn_quit = Button(frame, text="quit", command=root.quit)

frame.pack(pady=10, padx=10)
dropdown_day.grid(row=0, column=0)
dropdown_res.grid(row=0, column=1)
btn_select.grid(row=1, column=0)
btn_quit.grid(row=1, column=1)

root.mainloop()