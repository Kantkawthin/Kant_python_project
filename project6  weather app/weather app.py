'''
pip install geopy
pip install timezonefinder
pip install pytz

"+300+200":the position of the window on the screen. 
The +300 moves the window 300 pixels from the left edge of the screen,
and +200 moves it 200 pixels down from the top of the screen.

window.resizable(False,False) #this mean no resizing
window.resizable(horizontal resize,vertical resize)

place() , pack()  can use in different widget

cursor = hand2

side = TOP, BOTTOM, LEFT, RIGHT

font = poppins, Helvetica

#another way of using api
response = requests.get(api)
weather_data = json.loads(response.content)

'''

from tkinter import *
from PIL import ImageTk,Image
from geopy.geocoders import Nominatim
from tkinter import ttk,messagebox
from timezonefinder import TimezoneFinder
from datetime import datetime
import requests
import pytz   #python date time 
import json

window = Tk()
window.title("Weather App")
window.geometry("900x500+300+200")
window.resizable(False,False)

#function start

#search icon btn , getWeather function start
def getWeather():
    try:
        #get the address from text field inside search box
        city = textfield.get()
        #create obj_name (geolocator) to access geolocation functions
        geolocator = Nominatim(user_agent="geoApiWeather")
        #use geocode() function to find location for address
        location = geolocator.geocode(city)
        lat =location.latitude
        lon =location.longitude
        #Timezonefinder() =>to find region
        obj = TimezoneFinder()
        #use ( timezone_at method ) to find region at lat and lng
        result = obj.timezone_at(lng=location.longitude, lat=location.latitude)
        #print(result)
        
        #current date and time
        #define timezone for region
        region = pytz.timezone(result)
        #print(region)
        #use (datetime.now()) to generate local current date and time for region
        local_time = datetime.now(region)
        #current date and time H,M, AM/PM (12 hour format)
        current_time =local_time.strftime("%I:%M %p")
        #print(current_time)
        
        #display current time on screen
        name.config(text="CURRENT TIME")
        clock.config(text=current_time)
        
        #api  
        api_key ="ca7a84415dfba5467ecf2dbc3a81868c"
        #convert user input(city) to latidute(lat) and longitude(lon), use lat, lon api
        api = f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={api_key}"
        
        weather_data = requests.get(api).json()
        
        #To access a value in a dictionary,use square brackets ['dic_key']
        #To access an item in a list,use  square brackets [index_number]
        condition = weather_data['weather'][0]['main']
        description = weather_data['weather'][0]['description']
        temp = int(weather_data['main']['temp']-273.15)
        pressure = weather_data['main']['pressure']
        humidity = weather_data['main']['humidity']
        wind     = weather_data['wind']['speed']
        #api end
        
        #Display condition and temp degree celcius
        t.config(text=f'{temp}°')
        c.config(text=f'{condition} | FEELS Like {temp}°')
        
        #Display wind, pressure,humidity,description
        w.config(text=wind)
        h.config(text=humidity)
        d.config(text=description)
        p.config(text=pressure)
        
    except Exception as e:
        messagebox.showerror("Weather app","invalid Entry!!")

#getWeather() function end

    

#search start
#search image
search_img = ImageTk.PhotoImage(Image.open("image folder/search.png"))
search_image = Label(window,image=search_img)
search_image.place(x=50,y=20)
#text field inside search box
textfield = Entry(window,justify="center", width=17, font=("poppins",25,"bold"),bg="#404040", borderwidth=0,fg="white")
textfield.place(x=80, y=40)
textfield.focus()  #cursor in ur textbox 
#search icon btn
search_icon = ImageTk.PhotoImage(Image.open("image folder/search_icon.png"))
search_icon_btn = Button(window,image=search_icon,bg="#404040",borderwidth=0, cursor="hand2",command=getWeather)
search_icon_btn.place(x=430,y=34)
#search end

#display current time on screen start
#name 
name= Label(window,font=("arial",15,"bold"))
name.place(x=60,y=140)
#time
clock = Label(window,font=("arial",13))
clock.place(x=60, y=170)


# display condition and temp degree celcius
t = Label(window, font=("arial",70,"bold"), fg="#ee666d")
t.place(x=490, y=130)
c= Label(window,font=("arial",15,"bold"))
c.place(x=490,y=230)


#logo start
logo = ImageTk.PhotoImage(Image.open("image folder/logo.png"))
logo_image = Label(window,image=logo)
logo_image.place(x=220, y=100)
#logo end


#bottom bar start
#bottom bar image
bottom_bar = ImageTk.PhotoImage(Image.open("image folder/bar.png"))
bottom_bar_image = Label(window, image=bottom_bar)
bottom_bar_image.pack(padx=5,pady=5, side=BOTTOM)

#Text label inside the bottom bar
wind = Label(window,text="WIND", font=("Helvetica",15,"bold"), bg="#1ab5ef", fg="white")
wind.place(x=110, y=400)
humidity = Label(window,text="HUMIDITY", font=("Helvetica",15,"bold"), bg="#1ab5ef", fg="white")
humidity.place(x=235, y=400)
description = Label(window,text="DESCRIPTION", font=("Helvetica",15,"bold"), bg="#1ab5ef", fg="white")
description.place(x=430, y=400)
pressure = Label(window,text="PRESSURE", font=("Helvetica",15,"bold"), bg="#1ab5ef", fg="white")
pressure.place(x=680, y=400)

#Description of the text label
w = Label(window, text="...", font=("arial",14,"bold"), bg="#1ab5ef")
w.place(x=110, y=430)
h = Label(window, text="...", font=("arial",14,"bold"), bg="#1ab5ef")
h.place(x=235, y=430)
d = Label(window, text="...", font=("arial",14,"bold"), bg="#1ab5ef")
d.place(x=430, y=430)
p = Label(window, text="...", font=("arial",14,"bold"), bg="#1ab5ef")
p.place(x=680, y=430)

#bottom bar end

window.mainloop()
