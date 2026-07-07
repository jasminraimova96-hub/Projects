from turtle import Turtle
from random import randint

class Paddle(Turtle):
  def __init__(self, position):
    super().__init__()  
    self.penup()
    self.goto(position)
    self.shape("square") 
    self.color("white")
    self.shapesize(stretch_wid=5, stretch_len=1)
    self.speed("fastest")
  def up(self):
    self.sety(self.ycor() + 20)
  def down(self):
    self.sety(self.ycor() - 20) 



  