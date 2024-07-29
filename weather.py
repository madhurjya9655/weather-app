from tkinter import *
from tkinter import ttk
import requests


def get_data():
    city = city_name.get()
    try:
        data = requests.get(
            f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid=b4c2fbac3e45a7ff989d8719ab456c38&units=metric")
        data = data.json()

        w_label1.config(text=data['weather'][0]['main'])
        wb_label1.config(text=data['weather'][0]['description'])
        temp_label1.config(text=f"{data['main']['temp']}°C")
        pre_label1.config(text=f"{data['main']['pressure']} hPa")
    except Exception as e:
        print(f"Error: {e}")
        w_label1.config(text="Error")
        wb_label1.config(text="Error")
        temp_label1.config(text="Error")
        pre_label1.config(text="Error")


win = Tk()
win.title("Madhurjya Weather")
win.config(bg="blue")
win.geometry("500x570")

name_label = Label(win, text="Madhurjya's weather app", font=("Time New Roman", 25, "bold"))
name_label.place(x=25, y=50, height=50, width=450)

city_name = StringVar()
list_name = ["Andhra Pradesh", "Arunachal Pradesh", "Assam", "Bihar", "Chhattisgarh", "Goa", "Gujarat", "Haryana",
             "Himachal Pradesh", "Jammu and Kashmir", "Jharkhand", "Karnataka", "Kerala", "Madhya Pradesh",
             "Maharashtra", "Manipur", "Meghalaya", "Mizoram", "Nagaland", "Odisha", "Punjab", "Rajasthan", "Sikkim",
             "Tamil Nadu", "Telangana", "Tripura", "Uttar Pradesh", "Uttarakhand", "West Bengal",
             "Andaman and Nicobar Islands", "Chandigarh", "Dadra and Nagar Haveli", "Daman and Diu", "Lakshadweep",
             "National Capital Territory of Delhi", "Puducherry"]

com = ttk.Combobox(win, values=list_name, font=("Time New Roman", 20, "bold"), textvariable=city_name)
com.place(x=25, y=120, height=50, width=450)

done_button = Button(win, text="Click Here", font=("Time New Roman", 20, "bold"), command=get_data)
done_button.place(y=190, height=50, width=150, x=180)

w_label = Label(win, text="Weather Climate", font=("Time New Roman", 20))
w_label.place(x=25, y=260, height=50, width=210)

w_label1 = Label(win, text="", font=("Time New Roman", 20))
w_label1.place(x=250, y=260, height=50, width=210)

wb_label = Label(win, text="Weather Description", font=("Time New Roman", 17))
wb_label.place(x=25, y=330, height=50, width=210)

wb_label1 = Label(win, text="", font=("Time New Roman", 17))
wb_label1.place(x=250, y=330, height=50, width=210)

temp_label = Label(win, text="Temperature", font=("Time New Roman", 20))
temp_label.place(x=25, y=400, height=50, width=210)

temp_label1 = Label(win, text="", font=("Time New Roman", 20))
temp_label1.place(x=250, y=400, height=50, width=210)

pre_label = Label(win, text="Pressure", font=("Time New Roman", 20))
pre_label.place(x=25, y=470, height=50, width=210)

pre_label1 = Label(win, text="", font=("Time New Roman", 20))
pre_label1.place(x=250, y=470, height=50, width=210)

win.mainloop()