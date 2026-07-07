from tkinter import *
from quiz_brain import QuizBrain
THEME_COLOR = "#375362"

class QuizInterface:
  def __init__(self, quiz_brain: QuizBrain):
    self.quiz = quiz_brain
    self.window = Tk()
    self.window.title("Quizzler")
    self.window.config(padx= 20, pady=20,bg = THEME_COLOR, highlightthickness = 0 )
    self.canvas = Canvas(height=500,width=400,  bg="white")
    self.score_label = Label(text = "Score:0 ", bg = THEME_COLOR, highlightthickness = 0, fg= "white")
    true_image = PhotoImage(file = "./day34/images/true.png")
    false_image = PhotoImage(file = "./day34/images/false.png")
    self.right_button = Button(image = true_image, highlightthickness = 0, command= self.right_answer)
    self.right_button.grid(row=2,column= 0)
    self.false_button = Button(image = false_image, highlightthickness = 0, command= self.wrong_answer )
    self.false_button.grid(row=2,column= 1)
    self.score_label.grid(row=0,column=1, columnspan= 2)
    self.question_text = self.canvas.create_text(200, 250, width= 350 ,text= "smth", font=("Arial", 20, "italic"))
    self.canvas.grid(row=1, column=0, columnspan=2, padx=20,pady=20)
    self.get_next_question()


    self.window.mainloop()
  def get_next_question(self):
    if self.quiz.still_has_questions():
      self.canvas.config(bg="white")
      self.score_label.config(text=f"Score:{self.quiz.score}")
      q_text = self.quiz.next_question()
      self.canvas.itemconfig(self.question_text, text= q_text )
    else:
      self.canvas.itemconfig(self.question_text, text="You have reached the end of the quiz!")
      self.right_button.config(state="disabled")
      self.false_button.config(state="disabled")
  def right_answer(self):
    self.give_feedback(self.quiz.check_answer("True"))
    
  def wrong_answer(self):
    is_right = self.quiz.check_answer("False")
    self.give_feedback(is_right)

  def give_feedback(self, is_right):
    if is_right == "True":
      self.canvas.config(bg="green")
    elif is_right == "False":
      self.canvas.config(bg= "red")
    self.window.after(1000, self.get_next_question)