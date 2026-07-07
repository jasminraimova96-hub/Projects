from turtle import Turtle
FONT = ("Courier", 20, "normal")
class Score(Turtle):
  def __init__(self):
    super().__init__()
    self.color("black")
    self.score = 0
    self.penup()
    self.goto(-300, 260)   
    self.update_score() 
    self.hideturtle()
  def update_score(self):
    self.write(f" Level {self.score}", align="center",font = FONT)
  def increase_score(self):
    self.score += 1
    self.clear()
    self.update_score() 
  def game_over(self):
    self.penup()
    self.goto(0,0)  
    self.write(f"Game is over \n Your score {self.score}", align="center",font = ("Arial", 15, "normal") )