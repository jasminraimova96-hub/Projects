from tkinter import *
from tkinter import messagebox
from random  import randint, shuffle, choice
import json
import pandas
french_word = None
english_translation = None
known_words = []
unknown_words = []
#--------------------- BUTTON FUNCTIONS -----------------------
def right_button_function():
    global french_word, english_translation,random_row, words_data_frame
    known_words.append({
        "French": french_word,
        "English": english_translation
    })
    show_answer()
    window.after(3000, next_card)
def wrong_button_function():
    global french_word, english_translation
    unknown_words.append({
        "French": french_word,
        "English": english_translation
    })
    show_answer()
    window.after(3000, next_card)
    
def show_answer():
    global french_word, english_translation
    canvas.itemconfig(card_image, image=image_card_front)
    fr_eng_word_label.config(text = english_translation,bg="#FFFFFF",  highlightthickness=0 )
    text_label.config(text = "english",bg="#FFFFFF",  highlightthickness=0)
#-------------------------- SAVER -----------------------------
def saver():
  try:
    with open("known_words.json", "r" ) as data_file:       
      data = json.load(data_file) #reading data
  except FileNotFoundError:
    with open("known_words.json", "w" ) as data_file:  
      json.dump(known_words, data_file, indent = 4)#creating file
  else:
    data.update(known_words) #updating old data in a data
    with open("known_words.json", "w" ) as data_file:  
      json.dump(data, data_file, indent = 4)

  

#---------------------- WORDS FUNCTIONS -----------------------
data = pandas.read_csv("./day30/data/french_words.csv")
words_data_frame = pandas.DataFrame(data)
def random_word_generator():
  global french_word, english_translation
  random_row = words_data_frame.sample()
  french_word = random_row.french.values[0]
  english_translation = random_row.english.values[0]
  while french_word in [word["French"] for word in known_words]:
    random_row = words_data_frame.sample()
    french_word = random_row["French"].values[0]
    english_translation = random_row["English"].values[0]
random_word_generator()
def next_card():
  global french_word, english_translation
  random_word_generator()
  canvas.itemconfig(card_image, image=image_card_back)
  fr_eng_word_label.config(text= french_word, bg="#91C2AF")
  text_label.config(text = "french",bg="#91C2AF", highlightthickness=0)

   
#----------------------- VISUAL PART --------------------------
BACKGROUND_COLOR = "#B1DDC6"

window = Tk()
window.title("Flash Cards")
window.config(padx = 25,pady = 25, bg = BACKGROUND_COLOR)
canvas = Canvas(height = 300, width = 400, highlightthickness = 0)
image_card_back = PhotoImage(file="day30/data/card_back.png")
image_card_front = PhotoImage(file="day30/data/card_front.png")
image_right = PhotoImage(file="day30/data/right.png")
image_wrong = PhotoImage(file="day30/data/wrong.png")
card_image = canvas.create_image(200, 150, image=image_card_front)
canvas.grid(column =0, row = 0, columnspan= 2,rowspan=3, padx = 25,pady = 25)
canvas.itemconfig(card_image, image=image_card_back)
right_button = Button(image = image_right, height = 60, width = 60, highlightthickness=0, command= right_button_function)
right_button.grid(column = 1, row = 3)
wrong_button = Button(image = image_wrong, height = 60, width = 60, highlightthickness=0, command= wrong_button_function)
wrong_button.grid(column = 0, row = 3)
fr_eng_word_label = Label( text = french_word, font= ("Ariel" ,30," bold"),  bg="#91C2AF", highlightthickness=0 )
fr_eng_word_label.grid(column= 0, row = 1, columnspan= 2)
text_label = Label(text = "french", font= ("Ariel",20),  bg="#91C2AF", highlightthickness=0)
text_label.grid(column=0, row= 0, columnspan= 2 )

window.mainloop()
saver()


