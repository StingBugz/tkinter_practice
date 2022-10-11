import json
from tkinter import *
from json import *
from tkinter import messagebox
import requests


root = Tk()
root.title("Air Condition Now App")
icon_app = PhotoImage(file="./source/favicon/weather.png")
root.tk.call("wm","iconphoto",root._w, icon_app)
root.geometry("530x300")

def event_search():
    zipcode_number = search_entry.get()
    row_frame = 2
    try:
        request_api = requests.get(f"https://www.airnowapi.org/aq/observation/zipCode/current/?format=application/json&zipCode={zipcode_number}&distance=25&API_KEY=52428263-E48B-48AA-A395-7EC72BC6BC5C")
        data_api = json.loads(request_api.content)
        if data_api == []:
            messagebox.showwarning("Response API", "Data Empty.")
        
        else:
            #title label
            label_title = Label(root, text=f"Air Condition Now at {search_entry.get()}",font=("verdana", 15))
            label_title.grid(row=1, column=0, columnspan=7,sticky=W+E, pady=10)
            for i in range(len(data_api)):
                txt_area = data_api[i]["ReportingArea"]
                txt_AQI = "AQI " + str(data_api[i]["AQI"])
                txt_category = data_api[i]["Category"]["Name"]

                if txt_category == "Good":
                    bg_color = "#008000"
                elif txt_category == "Moderate":
                    bg_color = "#FFFF00"
                elif txt_category == "Unhealthy for Sensitive Groups":
                    bg_color = "#FFA500"
                elif txt_category == "Unhealthy":
                    bg_color = "#FF0000"
                elif txt_category == "Hazardous":
                    bg_color = "#800080"

                frame_data = Frame(root, background=bg_color, borderwidth=5)
                frame_data.grid(row=row_frame+i,column=0, columnspan=7, padx=10,pady=10,ipadx=30)

                label_area = Label(frame_data,text=txt_area, background=bg_color,width=10, padx=15, pady=5)
                label_AQI = Label(frame_data, text=txt_AQI, background=bg_color, width=10, padx=15, pady=5)
                label_category = Label(frame_data, text=txt_category, background=bg_color, width=10, padx=15, pady=5)
                label_area.grid(row=i, column=0)
                label_AQI.grid(row=i, column=1)
                label_category.grid(row=i, column=2)

    except Exception as e:
        messagebox.showerror("data","data not found")
        raise Exception from e

def resize_window():
    root.geometry(f"{width_entry.get()}x{height_entry.get()}")

#search
search_entry = Entry(root)
search_entry.grid(row=0, column=0,sticky=W+E+S+N, padx=5, pady=5)
btn_search = Button(root, text="Search Zipcode",font=("verdana", 8),command=event_search)
btn_search.grid(row=0,column=1, sticky=W+E+S+N)

#resize
label_w = Label(root, text="w:")
label_h = Label(root,text="h:")
width_entry = Entry(root, width=5)
width_entry.insert(0,"530")
height_entry = Entry(root, width=5)
height_entry.insert(0, "300")
btn_resize = Button(root,text="Resize", font=("verdana", 9), command=resize_window)

label_w.grid(row=0, column=2, padx=(10,5),sticky=W+E+S+N)
width_entry.grid(row=0, column=3, padx=(0,2), sticky=W+E+S+N)
label_h.grid(row=0, column=4, padx=(0,5),sticky=W+E+S+N)
height_entry.grid(row=0, column=5, padx=(0, 10),sticky=W+E+S+N)
btn_resize.grid(row=0, column=6, sticky=W+E+S+N)


root.mainloop()