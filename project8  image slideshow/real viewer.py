from tkinter import *
from PIL import ImageTk, Image

window = Tk()
window.title("Image Viewer")

# images convert to tkinter format
img1 = ImageTk.PhotoImage(Image.open("a.jpg"))
img2 = ImageTk.PhotoImage(Image.open("b.jpg"))
img3 = ImageTk.PhotoImage(Image.open("c.png"))
img4 = ImageTk.PhotoImage(Image.open("d.jpg"))
img5 = ImageTk.PhotoImage(Image.open("e.jpg"))

# image list
img_list = [img1, img2, img3, img4, img5]

# initialize the image number
image_number = 0

# image label
my_image = Label(image=img_list[image_number],width=850,height=478)
my_image.grid(row=0, column=0, columnspan=3)



def update_buttons():
    global button_back, button_forward
    # Disable back button if on the first image
    button_back.config(state=DISABLED if image_number == 0 else NORMAL)
    # Disable forward button if on the last image
    button_forward.config(state=DISABLED if image_number == len(img_list) - 1 else NORMAL)
    #image page number
    status = Label(window, text=f"Image {image_number + 1} of {len(img_list)}", bd=1, relief=SUNKEN, anchor=E,pady=5)
    status.grid(row=2, column=0, columnspan=3, sticky=W+E)

def forward():
    global image_number
    # Increase image_number
    image_number += 1
    # Remove previous image
    my_image.grid_forget()
    # Change to the new image
    my_image.config(image=img_list[image_number])
    my_image.grid(row=0, column=0, columnspan=3)
    update_buttons()

def back():
    global image_number
    # Decrease image_number
    image_number -= 1
    # Remove previous image
    my_image.grid_forget()
    # Change to the previous image
    my_image.config(image=img_list[image_number])
    my_image.grid(row=0, column=0, columnspan=3)
    update_buttons()

# buttons
button_back = Button(window, text="<<",bg="black", fg="white", command=back)
button_exit = Button(window, text="Exit Program",bg="black", fg="white", command=window.destroy)
button_forward = Button(window, text=">>",bg="black", fg="white", command=forward)

button_back.grid(row=1, column=0, pady=10, sticky='ew')
button_exit.grid(row=1, column=1, pady=10, sticky='ew')
button_forward.grid(row=1, column=2, pady=10, sticky='ew')

update_buttons()  # Initial button state update

window.mainloop()
