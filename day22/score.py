from turtle import Turtle

FONT = ("Courier", 20, "normal")
class Score(Turtle):
  def __init__(self,position):
    super().__init__()
    self.color("white")
    self.score = 0
    self.penup()
    self.goto(position)   
    self.update_score() 
    self.hideturtle()
  def update_score(self):
    self.write(f"{self.score}", align="center",font = FONT)
  def increase_score(self):
    self.score += 1
    self.clear()
    self.update_score() 
  def game_over(self, position):
    self.penup()
    self.goto(position)  
    self.write(f"Game is over \n Your score {self.score}", align="center",font = ("Arial", 15, "normal") )