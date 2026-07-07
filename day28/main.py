from tkinter import *

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer_id = None
# ---------------------------- TIMER RESET ------------------------------- # 
def timer_reset():
  window.after_cancel(timer_id)
  canvas.itemconfig(timer_text,text = "00:00")
  timer.config(text = "Timer") 
  mark.config(text = "")
  global reps
  reps = 0


# ---------------------------- TIMER MECHANISM ------------------------------- # 
def timer_starter():
  global reps
  reps += 1 
  if reps % 8 == 0:
    count_down(LONG_BREAK_MIN * 60)
    timer.config(text = "Long Break", fg = RED)  
  elif reps % 2 == 0:
    count_down(SHORT_BREAK_MIN * 60)
    timer.config(text = "Short Break", fg = PINK)
  else:
    count_down(WORK_MIN * 60)
    timer.config(text = "Work", fg = GREEN)

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
import math
def count_down(count):
  global reps
  global timer_id
  count_min = math.floor(count/60)
  count_sec = math.floor(count%60) 
  if count_sec < 10:
    count_sec = f"0{count_sec}"
  canvas.itemconfig(timer_text, text =f"{count_min}:{count_sec}" )
  if count > 0:
    timer_id = window.after(1000, count_down, count - 1)
  else:
    check_marks = ""
    for _ in range(reps // 2):
        check_marks += "✓"
    mark.config(text=check_marks)
    timer_starter()


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(padx= 100, pady = 50, bg = YELLOW)
canvas = Canvas(width = 200, height = 224, bg = YELLOW, highlightthickness = 0 )
tomato_img = PhotoImage(file = "./day28/tomato.png")
canvas.create_image(100, 112, image = tomato_img)
timer_text = canvas.create_text(100, 130, text ="00:00", fill = "white", font = (FONT_NAME, 35, "bold"))
canvas.grid(column = 2, row= 2)

timer = Label(text ="Timer", font = (FONT_NAME, 35, "bold"), fg = GREEN, bg =YELLOW, highlightthickness = 0)
timer.grid(column=2, row=1)
start = Button(text = "Start", font = (FONT_NAME, 10), command = timer_starter)
start.grid(column = 1, row =3)
reset = Button(text = "Reset", font = (FONT_NAME, 10), command = timer_reset)
reset.grid(column = 3, row =3)
mark = Label(font = (25), fg = GREEN, bg =YELLOW, highlightthickness = 0)
mark.grid(column= 2, row = 4)



window.mainloop()