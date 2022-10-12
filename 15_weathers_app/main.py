from tkinter import *
from tkinter import messagebox
from tkinter.font import BOLD
import requests
import json

root = Tk()
root.title("Weather App")
icon_root = PhotoImage(file="./source/favicon/weather-icon.png")
root.tk.call("wm","iconphoto", root._w, icon_root)


try:
    def event_search():
        frame_row = 2
        api_request = requests.get(f"https://www.airnowapi.org/aq/observation/zipCode/current/?format=application/json&zipCode={zip_entry.get()}&distance=5&API_KEY=52428263-E48B-48AA-A395-7EC72BC6BC5C")
        data_api = json.loads(api_request.content)
        #title
        if data_api == []:
            messagebox.showwarning("Response Api", "Data Empty.")
        else:
            title_label = Label(root, text=f"Air Quality Now at {zip_entry.get()}", font=("helvetica", 20, BOLD))
            title_label.grid(row=1, column=0, columnspan=2, sticky=W+E)
            for i in range(len(data_api)):
                data_reporting_area = data_api[i]["ReportingArea"]
                data_aqi = data_api[i]["AQI"]
                data_category =data_api[i]["Category"]["Name"]
                if data_category == "Good":
                    data_color = "#298600"
                elif data_category == "Moderate":
                    data_color = "#f9e909"
                elif data_category == "Unhealthy for Sensitive Groups":
                    data_color = "#f9e909"
                elif data_category == "Unhealthy":
                    data_color = "#f30000"
                elif data_category == "Hazardous":
                    data_color = "#4500E2"
                
                frame_data = LabelFrame(root)
                lbl_country = Label(frame_data, text=data_reporting_area, font="Helvetica 20",bg=data_color,width=20, padx=10, pady=5)
                lbl_aqi = Label(frame_data, text="AQI " + str(data_aqi), font="Helvetica 20",bg=data_color,width=20, padx=10, pady=5)
                lbl_category = Label(frame_data,text=data_category, font="Helvetica 20",bg=data_color,width=20, padx=10, pady=5)

                frame_data.grid(row=frame_row+i,column=0,padx=10,pady=10, columnspan=3)
                lbl_country.grid(row=i,column=0)
                lbl_aqi.grid(row=i,column=1)
                lbl_category.grid(row=i,column=2)


except Exception as e:
    messagebox.showerror("data",str(e))
    



#search section
zip_btn = Button(root, text="Search Zipcode", command=event_search)
zip_entry = Entry(root)
zip_entry.grid(row=0,column=0, padx=(5,3), pady=5, sticky=W+E+N+S)
zip_btn.grid(row=0,column=1, padx=3, sticky=W+E+N+S)

root.mainloop()