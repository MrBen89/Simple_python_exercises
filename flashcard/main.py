from tkinter import *
from random import choice, randint, shuffle
from tkinter import messagebox
import random
import pandas

BACKGROUND_COLOR = "#B1DDC6"
FONT_NAME = "Ariel"

window = Tk()
window.title("Lets learn French!")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)
window.minsize(800, 526)

front_img = PhotoImage(file="./images/card_front.png")
back_img = PhotoImage(file="./images/card_back.png")
cross_img = PhotoImage(file="./images/wrong.png")
tick_img = PhotoImage(file="./images/right.png")
current_word = "Trouve"
timer = ""


#------------------------------Generate words  --------------------------------#
try:
    word_data = pandas.read_csv("./data/to_learn.csv")
except FileNotFoundError:
    word_data = pandas.read_csv("./data/french_words.csv")
finally:
    word_data_frame = pandas.DataFrame(word_data)
    french_dict = word_data_frame.to_dict(orient="records")
    print(len(french_dict))

def generator():
    global current_word
    current_word=random.choice(french_dict)
    canvas.itemconfig(background, image=front_img)
    canvas.itemconfig(french_text, text="French", fill="black")
    canvas.itemconfig(french_word_text, text=current_word["French"], fill="black")
    call_timer()



# ------------------------------- Card Flip --------------------------------- #



def card_flip():
    canvas.itemconfig(background, image=back_img)
    canvas.itemconfig(french_text, text="English", fill="white")
    canvas.itemconfig(french_word_text, text=current_word["English"], fill="white")


def call_timer():
    global timer
    timer = window.after(3000, card_flip)



# ---------------------------- Remove card     ------------------------------- #

def remove_card():
    french_dict.remove(current_word)
    new_data_frame = pandas.DataFrame(french_dict)
    new_data_frame.to_csv("./data/to_learn.csv", index=False)
    generator()


# ---------------------------- UI SETUP ------------------------------- #

canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
background = canvas.create_image(400, 263, image=front_img)
french_text = canvas.create_text(400, 150, text="French", font=(FONT_NAME, 40, "italic"))
french_word_text = canvas.create_text(400, 263, text="trouve", font=(FONT_NAME, 60, "bold"))
canvas.grid(row=0, column=0, columnspan=2)

wrong_button = Button(image=cross_img, highlightthickness=0, command=generator)
wrong_button.grid(row=1, column=0)

right_button = Button(image=tick_img, highlightthickness=0, command=remove_card)
right_button.grid(row=1, column=1)


window.mainloop()
