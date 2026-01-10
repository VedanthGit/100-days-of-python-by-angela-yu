from random import choice
from tkinter import *
import pandas

BACKGROUND_COLOR = "#B1DDC6"
current_card = {}
to_learn = {}

try:
    updated_data = pandas.read_csv("./day 31/data/words_to_learn.csv")
except FileNotFoundError:
    data = pandas.read_csv("./day 31/data/french_words.csv") 
    to_learn = data.to_dict(orient="records")
else:
    to_learn = updated_data.to_dict(orient="records")

def next_card():
    if not to_learn:
        canvas.itemconfig(front_card_title, text="Done")
        canvas.itemconfig(front_card_word, text="All words learned 🎯")
        return
    global current_card, flip_timer
    window.after_cancel(flip_timer)
    current_card = choice(to_learn)
    canvas.itemconfig(card_background, image=front_image)
    canvas.itemconfig(front_card_title, text="French")
    canvas.itemconfig(front_card_word, text=current_card["French"])
    flip_timer = window.after(3000, func=flip_card)
    
def flip_card():
    canvas.itemconfig(front_card_title, text="English")
    canvas.itemconfig(front_card_word, text=current_card["English"])
    canvas.itemconfig(card_background, image=back_image)

def is_known():
    to_learn.remove(current_card)
    data = pandas.DataFrame(to_learn)
    data.to_csv("./day 31/data/words_to_learn.csv", index=False)
    next_card()

window = Tk()
window.title("FLAASHHMAN")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

flip_timer = window.after(3000, func=flip_card)

canvas = Canvas(width=800, height=526)

front_image = PhotoImage(file="./day 31/images/card_front.png")

back_image = PhotoImage(file="./day 31/images/card_back.png")

card_background = canvas.create_image(400,263, image=front_image)
front_card_title = canvas.create_text(400, 150, text="Title", font=("Ariel", 40, "italic"))
front_card_word = canvas.create_text(400, 263, text="Word", font=("Arial", 50, "bold"))

canvas.config(bg=BACKGROUND_COLOR)
canvas.grid(row = 0, column=0, columnspan=2)

right_image = PhotoImage(file="./day 31/images/right.png")
right_button = Button(image=right_image, highlightthickness=0, command=is_known)
right_button.grid(row=1, column=1)

wrong_image = PhotoImage(file="./day 31/images/wrong.png")  
wrong_button = Button(image=wrong_image, highlightthickness=0, command=next_card)
wrong_button.grid(row=1, column=0)

next_card()

window.mainloop()