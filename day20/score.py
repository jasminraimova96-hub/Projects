from turtle import Turtle
from food import Food
FONT = ("Arial", 24, "normal")
class Score(Turtle):
  def __init__(self):
    super().__init__()
    self.color("white")
    self.score = 0
    self.penup()
    self.goto(0,265)    
    self.hideturtle()
    with open("snake.txt", "r") as f:
      self.highscore = int(f.read())  
    self.update_score()
  def update_score(self):
    self.clear()
    self.write(f"Score: {self.score} High score: {self.highscore}", 
               align="center",
               font=FONT)
  def increase_score(self):
    self.score += 1
    self.update_score() 

  def reset_score(self):
    if self.score > self.highscore:
      self.highscore = self.score
      with open("snake.txt", "w") as f:
        f.write(f"{self.highscore}")
    self.score = 0
    self.update_score()
    



