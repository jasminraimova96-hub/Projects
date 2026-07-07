from tkinter import *
from tkinter import messagebox
from random  import randint, shuffle, choice
import pyperclip
import json
FONT_NAME = "Times New Roman"
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generator():
  letters = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
  numbers = ['0','1','2','3', '4', '5', '6', '7', '8','9']
  symbols = ['!','@','$', '%', '^', '&', '*','(', ')', '_']
  print('Welcome to password generator ')
  password_l = []
  letters_list = [password_l.append(choice(letters)) for char in range(randint(8,10))] 
  numbers_list = [password_l.append(choice(numbers)) for char in range(randint(2, 4))]
  symbols_list = [password_l.append(choice(symbols)) for char in range(randint(2, 4))] 
  shuffle(password_l)
  password = "".join(password_l)
  password_entry.insert(0, password)
  pyperclip.copy(password)

# ---------------------------- SAVE PASSWORD ------------------------------- #
def info_saver():
  website = website_entry.get()
  password = password_entry.get()
  email = email_entry.get()
  new_data = {website : {
    "email":  email,
    "password": password}
  }
  is_okay = messagebox.askokcancel(title = f"Website: {website}", message = f"These are details entered:\n Email: {email}\n Password: {password} \n Is it okey to save? ")
  if len(website) == 0 or len(password) == 0:
      messagebox.showerror(title = "OOPS", message = "Error, Please don't leave fields empty")   
  else:
    if is_okay:
      try:
        with open("password_data.json", "r" ) as data_file:       
          data = json.load(data_file) #reading data
      except FileNotFoundError:
        with open("password_data.json", "w" ) as data_file:  
          json.dump(new_data, data_file, indent = 4)
      else:
          data.update(new_data) #updating old data in a data
          with open("password_data.json", "w" ) as data_file:  
            json.dump(data, data_file, indent = 4) #writing new data
      finally:
        website_entry.delete(0, END)
        password_entry.delete(0, END) 
# ----------------------------- SEARCH -------------------------------- #
def search():
  website = website_entry.get()
  try:
    with open("password_data.json", "r") as data_file:
      website_data = json.load(data_file)
  except FileNotFoundError:
    messagebox.showinfo(text = "Error", message = "No Data File Found.")
  else:
    if website in website_data:
      messagebox.showinfo(title = f"{website}", message = f"These are details :\n Email: {website_data[website]["email"]} \n Password: {website_data[website]["password"]}") 
    else:  
      is_yes = messagebox.askyesno(title = f"OOPs", message = f"No details for this {website} exists, do you want to try again?")
      if is_yes:
        website_entry.delete(0, END)
    
# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx = 50,pady = 50)
canvas = Canvas()
canvas.config(height = 200, width = 200)
image_txt = PhotoImage(file = "logo.png")
canvas.create_image(100, 100, image = image_txt)
canvas.grid(column =1, row =0 )
website_label = Label(text= "Website:", font = (FONT_NAME, 12))
website_label.grid(column = 0, row = 1)
website_entry = Entry(width=30)
website_entry.grid(column=1, row=1)
website_entry.focus()
email_label = Label(text= "Email/Username:", font = (FONT_NAME, 12))
email_label.grid(column = 0, row =2)
email_entry = Entry(width=48)
email_entry.grid(column=1, row=2, columnspan=2)
email_entry.insert(0, "kotik@gmail.com")
password_label = Label(text= "Password:", font = (FONT_NAME, 12))
password_label.grid(column = 0, row = 3)
password_entry = Entry(width=30)
password_entry.grid(column=1, row=3)
generate_password_button = Button(text = "Generate Password", command = generator)
generate_password_button.grid(column=2, row=3)
add_button = Button(text = "Add", width = 36, command = info_saver)
add_button.grid(column=1, row=4, columnspan=2)
search_button = Button(text = "Search",font = (FONT_NAME, 12) , width = 12, command = search)
search_button .grid(column = 2, row = 1) 

window.mainloop()