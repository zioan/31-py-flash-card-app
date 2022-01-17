from tkinter import *
from tkinter import font
import pandas
import random

BACKGROUND_COLOR = "#B1DDC6"

data = pandas.read_csv("./data/translate_words.csv")
to_learn = data.to_dict(orient="records")
current_card = {}


def next_card():
    global current_card, flip_timer
    window.after_cancel(flip_timer)
    current_card = random.choice(to_learn)
    current_card["DE"]
    canvas.itemconfig(card_title, text="Deutsch", fill="black")
    canvas.itemconfig(card_word, text=current_card["DE"], fill="black")
    canvas.itemconfig(card_background, image=card_front_img)
    flip_timer = window.after(3000, func=flip_card)


def flip_card():
    canvas.itemconfig(card_title, text="English", fill="white")
    canvas.itemconfig(card_word, text=current_card["EN"], fill="white")
    canvas.itemconfig(card_background, image=card_back_img)


window = Tk()
window.title("Learn German")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

flip_timer = window.after(3000, func=flip_card)

canvas = Canvas(width=800, height=526)
card_front_img = PhotoImage(file="./images/card_front.png")
card_back_img = PhotoImage(file="./images/card_back.png")
card_background = canvas.create_image(400, 263, image=card_front_img)
canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
card_title = canvas.create_text(
    400, 150, text="", font=("Arial", 40, "italic"))
card_word = canvas.create_text(
    400, 263, text="", font=("Arial", 60, "bold"))
canvas.grid(row=0, column=0, columnspan=2)

cross_image = PhotoImage(file="./images/wrong.png")
unknown_buton = Button(
    image=cross_image, highlightthickness=0, command=next_card)
unknown_buton.grid(row=1, column=0)

check_image = PhotoImage(file="./images/right.png")
known_buton = Button(
    image=check_image, highlightthickness=0, command=next_card)
known_buton.grid(row=1, column=1)

next_card()
window.mainloop()
