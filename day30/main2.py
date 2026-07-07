from tkinter import *
from tkinter import messagebox
from random  import randint, shuffle, choice
import json
import pandas
BACKGROUND_COLOR = "#B1DDC6"
to_learn ={}
#----------------------PANDAS----------------------
try:
  data = pandas.read_csv("day30/data/words_to_learn.csv")
except FileNotFoundError:
  original_data = pandas.read_csv("./day30/data/french_words.csv")
  to_learn = original_data.to_dict(orient = "records")
else:
  to_learn =  data.to_dict(orient = "records")
#---------------- FUNCTIONS----------------
current_card = {}

def next_card():
    global current_card, flip_timer
    window.after_cancel(flip_timer)
    current_card = choice(to_learn)
    canvas.itemconfig(card_image, image=image_card_front)
    canvas.itemconfig(card_title, text="French", fill="black")
    canvas.itemconfig(card_word, text=current_card["french"], fill="black")
    flip_timer = window.after(3000, flip_card)
def flip_card():
    canvas.itemconfig(card_image, image=image_card_back)
    canvas.itemconfig(card_title, text="English", fill="white")
    canvas.itemconfig(card_word, text=current_card["english"], fill="white")
def is_known():
    to_learn.remove(current_card)
    data = pandas.DataFrame(to_learn)
    data.to_csv("day30/data/words_to_learn.csv", index= False)
    next_card()

window = Tk()
window.title("Flash Cards")
window.config(padx = 25,pady = 25, bg = BACKGROUND_COLOR)
flip_timer = window.after(3000, flip_card) 
canvas = Canvas(height = 300, width = 400, highlightthickness = 0)
image_card_back = PhotoImage(file="day30/data/card_back.png")
image_card_front = PhotoImage(file="day30/data/card_front.png")
image_right = PhotoImage(file="day30/data/right.png")
image_wrong = PhotoImage(file="day30/data/wrong.png")
card_image = canvas.create_image(200, 150, image=image_card_back)
card_title = canvas.create_text(200, 120, text="",font=("Arial", 20, "italic"))
card_word = canvas.create_text(200, 170, text="", font=("Arial", 20, "italic"))
canvas.grid(column =0, row = 0, columnspan= 2)
canvas.itemconfig(card_image, image=image_card_front)
right_button = Button(image = image_right, height = 60, width = 60, highlightthickness=0, command= is_known)
right_button.grid(column = 1, row = 3)
wrong_button = Button(image = image_wrong, height = 60, width = 60, highlightthickness=0, command= next_card)
wrong_button.grid(column = 0, row = 3)

next_card()
window.mainloop()