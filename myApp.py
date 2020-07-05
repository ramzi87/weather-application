from tkinter import *
from tkinter import messagebox
from PIL import ImageTk, Image
import requests

url = 'http://api.openweathermap.org/data/2.5/weather?q={}&appid={}'
api_key = '605777afd3d72eb5be67234616710a0c'

my_app = Tk()
my_app.title('Weather Application')
my_app.geometry('600x520+250+150')
my_app.resizable(width=False,height=False)

icon = PhotoImage(file='Status-weather-storm-day-icon.png')
my_app.call('wm','iconphoto',my_app._w,icon)

canvas1 = Canvas(my_app,width=600,height=520,bg='#c8ffee',relief='raise')
canvas1.pack()

canvas2 = Canvas(my_app,width=450,height=285,bg='#fcffae',bd=4)
canvas1.create_window(300,325,window=canvas2)

def get_weather(city):
	url_api = requests.get(url.format(city,api_key))
	if url_api:
		jsonData = url_api.json()
		city = jsonData['name']
		country = jsonData['sys']['country']
		temp_klv = jsonData['main']['temp']
		temp_celcius = temp_klv - 273.15
		temp_fehrenheit = (temp_klv-273.15)*9/5+32
		weather = jsonData['weather'][0]['main']
		pressure = jsonData['main']['pressure']
		description = jsonData['weather'][0]['description']

		final_result = (city,country,temp_celcius,temp_fehrenheit,weather,pressure,description)
		return final_result
	else:
		return None

def search():
	city = city_txt.get()
	weather_data = get_weather(city)
	if weather_data:
		lbl_location['text'] = (f'Location : {weather_data[0]} {weather_data[1]}')
		lbl_temp['text'] = ('Temperature : {:.2f}°C, {:.2f}°F'.format(weather_data[2],weather_data[3]))
		lbl_weather['text'] = (f'Weather : {weather_data[4]}')
		lbl_pressure['text'] = (f'Pressure : {weather_data[5]}')
		lbl_description['text'] = (f'Description : {weather_data[6]}')
	else:
		messagebox.showerror('Error',f'Can not find city {city}')


city_txt = StringVar()

city_ent = Entry(my_app,width=25,font=('Times',16),textvariable=city_txt)
canvas1.create_window(300,70,window=city_ent)

my_title = Label(my_app,text='Weather Application',font=('Times',14,'bold'),bg='#c8ffee')
canvas1.create_window(300,25,window=my_title)

search_btn = Button(my_app,text='Search',width=15,height=2,padx=4,pady=2,bd=2,font=('helvetica',10,'bold'),
	bg='brown',fg='white',command=search)
canvas1.create_window(300,130,window=search_btn)

lbl_location = Label(my_app,text='',bg='#fcffae')
lbl_location.config(font=('Times',14))
canvas2.create_window(230,45,window=lbl_location)

lbl_temp = Label(my_app,text='',bg='#fcffae')
lbl_temp.config(font=('Times',14))
canvas2.create_window(230,95,window=lbl_temp)

lbl_weather = Label(my_app,text='',bg='#fcffae')
lbl_weather.config(font=('Times',14))
canvas2.create_window(230,145,window=lbl_weather)

lbl_pressure = Label(my_app,text='',bg='#fcffae')
lbl_pressure.config(font=('Times',14))
canvas2.create_window(230,195,window=lbl_pressure)

lbl_description = Label(my_app,text='',bg='#fcffae')
lbl_description.config(font=('Times',14))
canvas2.create_window(230,245,window=lbl_description)

image1 = Image.open('Status-weather-showers-day-icon.png')
image1 = image1.resize((80,80))
img1 = ImageTk.PhotoImage(image1)

image2 = Image.open('Status-weather-storm-day-icon.png')
image2 = image2.resize((80,80))
img2 = ImageTk.PhotoImage(image2)

img_lbl_1 = Label(my_app,width=80,height=80,image=img1)
canvas1.create_window(44,44,window=img_lbl_1)

img_lbl_2 = Label(my_app,width=80,height=80,image=img2)
canvas1.create_window(556,44,window=img_lbl_2)


my_app.mainloop()