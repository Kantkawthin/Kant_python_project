from tkinter import *
from tkinter import ttk,messagebox
from PIL import ImageTk, Image
from geopy.geocoders import Nominatim
from timezonefinder import TimezoneFinder
from datetime import *
import pytz
import requests
import json

window = Tk()
window.title("Weather Forecast")
window.geometry("900x600+300+100")
window.configure(bg="#00a1f1")

#getWeather() function start
def getWeather():
    #get address name from entry "textfield" box
    city = textfield.get()
    #create obj_name (geolocator) to access geolocation functions
    geolocator = Nominatim(user_agent="mygeoapi")
    #use geocode() function to find location for address
    location = geolocator.geocode(city)
    lat = location.latitude
    lon = location.longitude
    #Timezonefinder() =>to find region
    obj = TimezoneFinder()
    #use ( timezone_at method ) to find region at (lat and lng) keyword
    result = obj.timezone_at(lng=location.longitude, lat=location.latitude)
    print(result)
    
    #current date and time
    #define timezone for region
    region = pytz.timezone(result)
    #use (datetime.now()) to generate local current date and time for region
    local_time = datetime.now(region)
    #current date and time Y-M-D  H,M, AM/PM (12 hour format)
    current_date = local_time.strftime("%d-%m-%Y")
    current_time = local_time.strftime("%I:%M %p")
    #display
    date_label.config(text=current_date)
    time_label.config(text=current_time)
    region_label.config(text=region)
    lat_lng_label.config(text=f'{round(location.latitude,4)}°N / {round(location.longitude,4)}°E')

    

    #Accuweather api start
    api_key = "JkVgdbNW0HVrpfaAXLBe9ojntcsHGQNf"
    
    lat = location.latitude
    lon = location.longitude

    #find location key with geoposition
    location_key_api = f"http://dataservice.accuweather.com/locations/v1/cities/geoposition/search?apikey={api_key}&q={lat},{lon}"
    location_data = requests.get(location_key_api).json()
    
    #get location_key  
    location_key = location_data['Key']
    print(location_key)
    
    #current weather start 
    #api request,respond
    current_weather_api = f"http://dataservice.accuweather.com/currentconditions/v1/{location_key}?apikey={api_key}"
    current_weather_data= requests.get(current_weather_api).json()
    
    
    #weather icon, temperature,description info for current weather
    current_icon=current_weather_data[0]['WeatherIcon']
    temp =current_weather_data[0]['Temperature']['Metric']['Value']
    description = current_weather_data[0]['WeatherText']
    
    #display weather icon, temperature,description
    #weather icon
    icon_img = ImageTk.PhotoImage(Image.open(f'accuweather icon/{current_icon}-s.png'))
    icon.config(image=icon_img)
    icon.image=icon_img  #prevent garbage problem
    #temperature
    t.config(text=f'{temp}°C')
    #description
    d.config(text=f'{description}')
    #current weather end
    

    #forecast for 5 days start
    #api request,respond
    forecast_weather_api = f"http://dataservice.accuweather.com/forecasts/v1/daily/5day/{location_key}?apikey={api_key}"
    forecast_weather_data= requests.get(forecast_weather_api).json()
    
    
    #display bottom
    #days for each box start
    #1
    first = datetime.now()
    day1.config(text=first.strftime("%A"))
    #2
    second = first+timedelta(days=1)  #add 1 day to the current day
    day2.config(text=second.strftime("%A"))
    #3
    third = second+timedelta(days=1)  #add 1 day to the current day
    day3.config(text=third.strftime("%A"))
    #4
    fourth = third+timedelta(days=1)  #add 1 day to the current day
    day4.config(text=fourth.strftime("%A"))
    #5
    fifth = fourth+timedelta(days=1)  #add 1 day to the current day
    day5.config(text=fifth.strftime("%A"))
    #days for each box end
    

    #weather_icon for each box start
    #1
    weather_icon1 = forecast_weather_data['DailyForecasts'][0]['Day']['Icon']
    img1 = ImageTk.PhotoImage(Image.open(f"accuweather icon/{weather_icon1}-s.png"))
    day1_image.config(image=img1)
    day1_image.image = img1
    #2
    weather_icon2 = forecast_weather_data['DailyForecasts'][1]['Day']['Icon']
    photo2 = Image.open(f"accuweather icon/{weather_icon2}-s.png")
    resize_photo = photo2.resize((60,35))   #resize((width,height))
    img2 = ImageTk.PhotoImage(resize_photo)
    day2_image.config(image=img2)
    day2_image.image = img2
    #3
    weather_icon3 = forecast_weather_data['DailyForecasts'][2]['Day']['Icon']
    photo3 = Image.open(f"accuweather icon/{weather_icon3}-s.png")
    resize_photo = photo3.resize((60,35))   #resize((width,height))
    img3 = ImageTk.PhotoImage(resize_photo)
    day3_image.config(image=img3)
    day3_image.image = img3
    #4
    weather_icon4 = forecast_weather_data['DailyForecasts'][3]['Day']['Icon']
    photo4 = Image.open(f"accuweather icon/{weather_icon4}-s.png")
    resize_photo = photo4.resize((60,35))   #resize((width,height))
    img4 = ImageTk.PhotoImage(resize_photo)
    day4_image.config(image=img4)
    day4_image.image = img4
    #5
    weather_icon5 = forecast_weather_data['DailyForecasts'][4]['Day']['Icon']
    photo5 = Image.open(f"accuweather icon/{weather_icon5}-s.png")
    resize_photo = photo5.resize((60,35))   #resize((width,height))
    img5 = ImageTk.PhotoImage(resize_photo)
    day5_image.config(image=img5)
    day5_image.image = img5
    
    #weather_icon for each box end
    

    #day/ night temperature start
    
    #day1
    #day & convert F to C
    d_temp1= float((forecast_weather_data['DailyForecasts'][0]['Temperature']['Maximum']['Value']-32)/1.8)
    #night & convert F to C
    n_temp1= float((forecast_weather_data['DailyForecasts'][0]['Temperature']['Minimum']['Value']-32)/1.8)
    #display day1
    day1_temp.config(text=f"Day:{round(d_temp1,2)}°C\n Night:{round(n_temp1,2)}°C")

    #day2
    #day & convert F to C
    d_temp2= float((forecast_weather_data['DailyForecasts'][1]['Temperature']['Maximum']['Value']-32)/1.8)
    #night & convert F to C
    n_temp2= float((forecast_weather_data['DailyForecasts'][1]['Temperature']['Minimum']['Value']-32)/1.8)
    #display day2
    day2_temp.config(text=f"Day:{round(d_temp2,2)}°C\n Night:{round(n_temp2,2)}°C")
    
    #day3
    #day & convert F to C
    d_temp3= float((forecast_weather_data['DailyForecasts'][2]['Temperature']['Maximum']['Value']-32)/1.8)
    #night & convert F to C
    n_temp3= float((forecast_weather_data['DailyForecasts'][2]['Temperature']['Minimum']['Value']-32)/1.8)
    #display day3
    day3_temp.config(text=f"Day:{round(d_temp3,2)}°C\n Night:{round(n_temp3,2)}°C")
    
    #day4
    #day & convert F to C
    d_temp4= float((forecast_weather_data['DailyForecasts'][3]['Temperature']['Maximum']['Value']-32)/1.8)
    #night & convert F to C
    n_temp4= float((forecast_weather_data['DailyForecasts'][3]['Temperature']['Minimum']['Value']-32)/1.8)
    #display day4
    day4_temp.config(text=f"Day:{round(d_temp4,2)}°C\n Night:{round(n_temp4,2)}°C")
    
    #day5
    #day & convert F to C
    d_temp5= float((forecast_weather_data['DailyForecasts'][4]['Temperature']['Maximum']['Value']-32)/1.8)
    #night & convert F to C
    n_temp5= float((forecast_weather_data['DailyForecasts'][4]['Temperature']['Minimum']['Value']-32)/1.8)
    #display day5
    day5_temp.config(text=f"Day:{round(d_temp5,2)}°C\n Night:{round(n_temp5,2)}°C")
    
    #day/ night temperature end
    
    

    
    #forecast for 5 days end
    
    #Accuweather api end
    
                         
#getWeather() function end
    
    

#title icon
title_icon = ImageTk.PhotoImage(Image.open("image/logo.png"))
window.iconphoto(False, title_icon)

#date and time display start
#frame
date_time_frame = Frame(window,width=200, height=200,bg="#00a1f1")
date_time_frame.place(x=80, y=40)
#time text
time_label=Label(date_time_frame,font=("poppins",30,"bold"), fg="white",bg="#00a1f1")
time_label.place(x=0,y=0)
#date text
date_label = Label(date_time_frame,font=("poppins",12), fg="white",bg="#00a1f1")
date_label.place(x=50,y=50)
#date and time display end

#region and latitude-longitude start
#frame
location_region_frame = Frame(window,width=270, height=100, bg="#00a1f1")
location_region_frame.place(x=600, y=40)
#region
region_label = Label(location_region_frame,font=("poppins",25,"bold"), fg="white",bg="#00a1f1")
region_label.pack()
#lat_lng
lat_lng_label = Label(location_region_frame,font=("poppins",12), fg="white",bg="#00a1f1")
lat_lng_label.pack()
#region and latitude-longitude end


#display box and info start with icon
#frame
info_frame = Frame(window,width=220,height=210,bg="#203243")
info_frame.place(x=80,y=160)
#current_icon
photo = ImageTk.PhotoImage(Image.open("accuweather icon/load.webp"))
icon = Label(info_frame,image=photo,bg="#203243")
icon.place(relx=0.5, y=15,anchor="n")
#temperature, description text Label
Label(info_frame,text="Temperature" ,font=("Helvetica",14,"bold"),fg="white", bg="#203243").place(relx=0.5,y=80, anchor="n")
Label(info_frame,text="Description" ,font=("Helvetica",14,"bold"),fg="white", bg="#203243").place(relx=0.5,y=145,anchor="n")
#temperature, description text info
t = Label(info_frame,text=".....",font=("Helvetica",11),fg="white",bg="#203243")
t.place(relx=0.5,y=105,anchor="n")
d = Label(info_frame,text=".....",font=("Helvetica",11),fg="white",bg="#203243")
d.place(relx=0.5,y=170,anchor="n")                       
#display box and info end

#search bar start
#search bar
search_image = ImageTk.PhotoImage(Image.open("image/Rounded Rectangle 3.png"))
search_bar = Label(window,image=search_image,bg="#00a1f1")
search_bar.place(x=400, y=220)
#cloud icon
cloud_image = ImageTk.PhotoImage(Image.open("image/search image.png"))
cloud = Label(window,image=cloud_image,bg="#203243")
cloud.place(x=420, y=225)
#textfield
textfield = Entry(window,width=15, font=('poppins',16),bg="#203243",border=0,justify="center",fg="white")
textfield.place(x=460, y=230)
textfield.focus()
#search button
search_icon = ImageTk.PhotoImage(Image.open("image/search icon.png"))
search_button = Button(window,image=search_icon,bg="#203243",border=0,cursor="hand2",command=getWeather)
search_button.place(x=700,y=225)
#search bar end


#bottom frame start
#bottom frame
frame_bottom = Frame(window,height=200,bg="#212120")
frame_bottom.pack(fill="x",side="bottom")
#Day & Night display box
day_night = ImageTk.PhotoImage(Image.open("image/Rounded Rectangle 2.png"))
day_night_box = Label(frame_bottom,image=day_night,bg="#212120")
day_night_box.place(x=70, y=30)
#6 boxes
Box_img = ImageTk.PhotoImage(Image.open("image/long rectangle.png"))
Label(frame_bottom, image=Box_img, bg="#212120").place(x=350, y=40)
Label(frame_bottom, image=Box_img, bg="#212120").place(x=480, y=40)
Label(frame_bottom, image=Box_img, bg="#212120").place(x=610, y=40)
Label(frame_bottom, image=Box_img, bg="#212120").place(x=740, y=40)


#bottom boxes data start
#1 big box
big_box = Frame(frame_bottom,width=230,height=130,bg="#282829")
big_box.place(x=75, y=35)
#day1_image
day1_image = Label(big_box,bg="#282829")
day1_image.place(x=8, y=48)
#day1 date
day1 = Label(big_box,font=("arial",19,"bold"),bg="#282829",fg="white")
day1.place(x=80, y=5)
#day1 temperature(day/night)
day1_temp = Label(big_box,font=("arial",12,"bold"),bg="#282829",fg="#00a1f1")
day1_temp.place(x=80, y=60)


#2 small box
small_box1 = Frame(frame_bottom,width=70,height=115, bg="#282829")
small_box1.place(x=355,y=45)
#day2_image
day2_image = Label(small_box1,  bg="#282829")
day2_image.place(relx=0.5, y=30, anchor="n")
#day2 date
day2 = Label(small_box1,font=("arial",9),bg="#282829",fg="white")
day2.place(relx=0.5, y=4, anchor="n")   #relx=0.5 , Positions the label at 50% of the width of big_box.
#day2 temperature(day/night)
day2_temp = Label(small_box1,font=("arial",7),bg="#282829",fg="white")
day2_temp.place(relx=0.5, y=75,anchor="n")


#3 small box
small_box2 = Frame(frame_bottom,width=70,height=115, bg="#282829")
small_box2.place(x=485,y=45)
#day3_image
day3_image = Label(small_box2,bg="#282829")
day3_image.place(relx=0.5,y=30, anchor="n")
#day3 date
day3 = Label(small_box2,font=("arial",9),bg="#282829",fg="white")
day3.place(relx=0.5, y=4, anchor="n")
#day3 temperature(day/night)
day3_temp = Label(small_box2,font=("arial",7),bg="#282829",fg="white")
day3_temp.place(relx=0.5, y=75,anchor="n")


#4 small box
small_box3 = Frame(frame_bottom,width=70,height=115, bg="#282829")
small_box3.place(x=615,y=45)
#day4_image
day4_image = Label(small_box3,bg="#282829")
day4_image.place(relx=0.5,y=30, anchor="n")
#day4 date
day4 = Label(small_box3,font=("arial",9),bg="#282829",fg="white")
day4.place(relx=0.5, y=4, anchor="n")
#day4 temperature(day/night)
day4_temp = Label(small_box3,font=("arial",7),bg="#282829",fg="white")
day4_temp.place(relx=0.5, y=75,anchor="n")


#5 small box
small_box4 = Frame(frame_bottom,width=70,height=115, bg="#282829")
small_box4.place(x=745,y=45)
#day5_image
day5_image = Label(small_box4,bg="#282829")
day5_image.place(relx=0.5,y=30, anchor="n")
#day5 date
day5 = Label(small_box4,font=("arial",9),bg="#282829",fg="white")
day5.place(relx=0.5, y=4, anchor="n")
#day5 temperature(day/night)
day5_temp = Label(small_box4,font=("arial",7),bg="#282829",fg="white")
day5_temp.place(relx=0.5, y=75,anchor="n")


#bottom frame end


window.mainloop()
