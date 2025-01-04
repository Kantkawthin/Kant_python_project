'''
#resize_photo 
open photo =>photo = Image.open("")
photo.resize((50,50))   
photo.resize((width,height))

#50% x,y
widget.place(relx=0.5, rely=0.5, anchor="n")
'''


from tkinter import *
from random import randint
from PIL import ImageTk, Image

window =Tk()
window.title("Tarot card generator")
window.geometry("320x460+300+100")
window.configure(bg="#282823")



#card
card1 = ImageTk.PhotoImage(Image.open("tarot/death.png"))
card2 = ImageTk.PhotoImage(Image.open("tarot/judgement.png"))
card3 = ImageTk.PhotoImage(Image.open("tarot/justice.png"))
card4 = ImageTk.PhotoImage(Image.open("tarot/strength.png"))
card5 = ImageTk.PhotoImage(Image.open("tarot/temperance.png"))
card6 = ImageTk.PhotoImage(Image.open("tarot/the-chariot.png"))
card7 = ImageTk.PhotoImage(Image.open("tarot/the-devil.png"))
card8 = ImageTk.PhotoImage(Image.open("tarot/the-emperor.png"))
card9 = ImageTk.PhotoImage(Image.open("tarot/The-Empress.png"))
card10 = ImageTk.PhotoImage(Image.open("tarot/the-fool.png"))
card11 = ImageTk.PhotoImage(Image.open("tarot/the-hanged-man.png"))
card12 = ImageTk.PhotoImage(Image.open("tarot/the-hermit.png"))
card13 = ImageTk.PhotoImage(Image.open("tarot/the-high-priestess.png"))
card14 = ImageTk.PhotoImage(Image.open("tarot/the-lovers.png"))
card15 = ImageTk.PhotoImage(Image.open("tarot/the-magician.png"))
card16 = ImageTk.PhotoImage(Image.open("tarot/the-moon.png"))
card17 = ImageTk.PhotoImage(Image.open("tarot/the-star.png"))
card18 = ImageTk.PhotoImage(Image.open("tarot/the-sun.png"))
card19 = ImageTk.PhotoImage(Image.open("tarot/the-tower.png"))
card20 = ImageTk.PhotoImage(Image.open("tarot/the-world.png"))
card21 = ImageTk.PhotoImage(Image.open("tarot/wheel-of-fortune.png"))

#card dictionary
card_answer ={
                card1 : "Yes",
                card2 : "Neutral/Yes",
                card3 : "Neutral",
                card4 : "Yes",
                card5 : "Yes",
                card6 : "Yes",
                card7 : "No",
                card8 : "Yes",
                card9 : "Yes",
                card10: "Yes",
                card11: "Maybe",
                card12: "Yes/100%",
                card13: "Yes",
                card14: "Yes/Later",
                card15: "Yes",
                card16: "No",
                card17: "Yes/100%",
                card18: "Yes/100%",
                card19: "No",
                card20: "Yes/100%",
                card21: "Yes"
    }



#tarot_card function start
def tarot_card():

    #change the window size
    window.geometry("320x570+300+100")
    
    cards = [card1,card2,card3,card4,card5,card6,
             card7,card8,card9,card10,card11,card12,
             card13,card14,card15,card16,card17,card18,
             card19,card20,card21]

    #convert list to set to remove duplicate 
    check_cards = set(cards)

    #convert again to list to generate random
    unique_cards = list(check_cards)
    
    #find the total number on list to generate random number
    our_number = len(unique_cards)-1
   
    #random  number generate
    random_number = randint(0, our_number)
    
    #random card 
    random_card = cards[random_number]    # cards[0]
    
    
    #disply  tarot card on screen 
    card_choose.config(image=random_card)
    card_choose.image = random_card
    card_choose.place(rely=0.0)

    #answer
    #unhide answer_label widget and display the answer
    answer_label.config(text=f"Answer:\n{card_answer[random_card]}",bg="#5e5c56")   #card_answer['card1']
    answer_label.pack(side="bottom",pady=(0,20))
    
#tarot_card function end

#ask again 
def ask_again():
    card_choose.config(image=question,bg="#282823")
    card_choose.place(relx=0.5, rely=0.4, anchor="n")

    #hide the answer_label widget
    answer_label.pack_forget()

    #back to the original window size
    window.geometry("320x460+300+100")


#display start
#text
label = Label(window, text="Yes/No Tarot Card Reading",fg="#f5e8b6",font=("poppins",15,"bold"),bg="#282823")
label.place(relx=0.5, y=20, anchor="n")
#click fortune button
choose_btn = Button(window,text="Click Your Fortune", font=("poppins",14,"bold"),bg="#edbe5f",command=tarot_card)
choose_btn.place(relx=0.5, y=337, anchor="n")
#ask again button
clear_btn = Button(window,text="Ask Next Question",padx=4, font=("poppins",14,"bold"),bg="#edbe5f",command=ask_again)
clear_btn.place(relx=0.5, y=390, anchor="n")
#Answer box
answer_label= Label(window,fg="white",padx=60, pady=15,font=("poppins",13,"bold"),bg="#282823")
answer_label.pack_forget()     #hide the widget


#tarot card start
#bg_frame start
#bg_img start
b_img = Image.open("image/long rectangle.png")
resize_bImg = b_img.resize((125,230))
bg_photo = ImageTk.PhotoImage(resize_bImg)
#bg_img display
background_img = Label(window,image=bg_photo, bg="#edbe5f")
background_img.place(relx=0.5, y=90, anchor="n")
#bg_img end
#frame
frame = Frame(window,width=120,height=225,bg="#282823")
frame.place(relx=0.5, y=93, anchor="n")
#bg_frame end

#card_choose start
#question mark
question_icon = Image.open("image/question mark.png")
resized = question_icon.resize((50,50))
question = ImageTk.PhotoImage(resized)
#card choose
card_choose = Label(frame,image=question,bg="#282823")
card_choose.place(relx=0.5, rely=0.4, anchor="n")
#card_choose end
#tarot card end

#display end


window.mainloop()

