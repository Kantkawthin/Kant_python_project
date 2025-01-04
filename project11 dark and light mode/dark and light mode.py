from tkinter import *
from PIL import ImageTk, Image

window = Tk()
window.title("Dark and Light mode")
window.geometry("300x300+300+200")
window.config(bg="white")

#day image
day = ImageTk.PhotoImage(Image.open("image/day.png"))
night = ImageTk.PhotoImage(Image.open("image/night.png"))


#light_click function
def light_click():
    btn_light.place_forget()
    btn_dark.place(relx=0.5, y=50, anchor="n")
    window.config(bg="black")

#dark_click function
def dark_click():
    btn_dark.place_forget()
    btn_light.place(relx=0.5, y=50, anchor="n")
    window.config(bg="white")
    

#light
btn_light = Button(window, image=day,bg="white", bd=0,activebackground="white", command=light_click)
btn_light.place(relx=0.5, y=50, anchor="n")

#dark
btn_dark = Button(window, image=night, bg="black", bd=0,activebackground="black",command=dark_click)
btn_dark.place_forget()

window.mainloop()