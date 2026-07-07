from tkinter import *
window = Tk()
window.title("Miles to Kilometers")
window.minsize(width=200, height=100)
window.config(padx = 50,pady = 25)
def button_clicked():
  new_text = input.get()
  label.config(text = new_text)

def calculate():
  miles = float(inputt.get())
  km = miles * 1.60934
  label.config(text = km)
miles = Label(text="Miles", font=("Arial",10))
miles.grid(column=4, row=0)
equal = Label(text="Is equal to", font=("Arial",10))
equal.grid(column=2, row=2)
label = Label(text="0", font=("Arial",10))
label.grid(column=3, row=2)
km = Label(text="km", font=("Arial",10))
km.grid(column=4, row=2)
button = Button(text="Calculate", command=calculate)
button.grid(column=3, row=3)
inputt = Entry(width=10)
inputt.grid(column=3, row=0)


window.mainloop()
