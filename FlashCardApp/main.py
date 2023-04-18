import random
from tkinter import *
import pandas
from random import choice

BACKGROUND_COLOR = "#B1DDC6"
FONT_NAME = "Ariel"
to_learn={}
# ---------------------------- SAVE CSV ------------------------------- #


# ---------------------------- GET WORD ------------------------------- #
try:
    data_frame = pandas.read_csv("data/words_to_learn.csv")
except FileNotFoundError:
    original_data=pandas.read_csv("data/russian_words.csv")
    to_learn =original_data.to_dict(orient="records")
else:
    to_learn = data_frame.to_dict(orient="records")

def next_card():
    global current_card,flip_timer
    window.after_cancel(flip_timer)
    canvas.itemconfig(canvas_image, image=f_img)
    current_card=choice(to_learn)
    canvas.itemconfig(f_title, text="Russian",fill="black")
    canvas.itemconfig(f_word, text=current_card["Russian"],fill="black")
    flip_timer=window.after(3000, func=flip_card)

def flip_card():
    canvas.itemconfig(canvas_image,image=b_img)
    canvas.itemconfig(f_title, text="English",fill="white")
    canvas.itemconfig(f_word, text=current_card["English"],fill="white")

def known_word():
    to_learn.remove(current_card)
    next_card()
    data=pandas.DataFrame(to_learn)
    data.to_csv("data/words_to_learn.csv", index=False)

# ---------------------------- UI SETUP -------------------------------
window=Tk()
window.title("Russian Flash cards")
window.config(padx=50,pady=50,bg=BACKGROUND_COLOR)
flip_timer=window.after(3000, func=flip_card)


canvas=Canvas(width=800, height=526, background=BACKGROUND_COLOR, highlightthickness=0)
f_img=PhotoImage(file="./images/card_front.png")
b_img=PhotoImage(file="./images/card_back.png")
canvas_image=canvas.create_image(400, 263, image=f_img)
canvas.grid(row=0, column=0, columnspan=2)

f_title=canvas.create_text(400, 150, text="", fill="black", font=(FONT_NAME, 40, "italic"))
f_word=canvas.create_text(400, 263, text="", fill="black", font=(FONT_NAME, 60, "bold"))


x_img=PhotoImage(file="./images/wrong.png")
unknown_button=Button(image=x_img, highlightthickness=0, command=next_card)
unknown_button.grid(row=1, column=0)

y_img=PhotoImage(file="./images/right.png")
known_button=Button(image=y_img, highlightthickness=0,command=known_word)
known_button.grid(row=1, column=1)
next_card()

window.mainloop()