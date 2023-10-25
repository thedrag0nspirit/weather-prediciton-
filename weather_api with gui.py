import tkinter as tk
import requests
import time


def getweather(master):
    city=textfield.get()
    api="https://api.openweathermap.org/data/2.5/weather?q=" + city +"&appid=4f6a7388333d357c170b6a744809098f"
    json_data=requests.get(api).json()
    condition=json_data["weather"][0]['main']
    temp=int(json_data['main']['temp']-273)
    min_temp=int(json_data['main']['temp']-273)
    max_temp=int(json_data['main']['temp']-273)
    pressure=json_data['main']['pressure']
    humidity=json_data['main']['humidity']
    wind=json_data['wind']['speed']
    sunrise=time.strftime("%I:%M:%S", time.gmtime(json_data['sys']['sunrise']-19800))
    sunset=time.strftime("%I:%M:%S", time.gmtime(json_data['sys']['sunset']-19800))

    final_info=condition+ " \n" + str(temp) + "°C"
    final_data="\n" + "Max Temp" + str(max_temp)+ "\n" + "Min Temp" + str(min_temp) + "\n" + "Pressure" + str(pressure) + "\n" + "Humidity" + str(humidity) + "\n" + "Wind Speed" + str(wind) + "\n" + "Sunrise" + sunrise + "\n" + "Sunset" + sunset
    label1.config(text=final_info)
    label2.config(text=final_data)


#Gui
master=tk.Tk()
master.title("Weather App")


#to enter location 
textfield=tk.Entry(master, font=("calibri Bold",20))
textfield.pack(pady=20)
textfield.focus()
textfield.bind('<Return>', getweather)

#Labels
label1=tk.Label(master, font=("calibri bold",40))
label1.pack()
label2=tk.Label(master, font=("Calibri bold", 20))
label2.pack()



master.mainloop()