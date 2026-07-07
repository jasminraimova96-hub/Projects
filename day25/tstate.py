from turtle import Turtle
class State(Turtle):
  def __init__(self):
    super().__init__()
    self.hideturtle()
    self.penup()
    self.states = []
  def state_position(self, name, x, y):
    self.goto(x,y)
    self.write(name, align="center", font=("Arial", 8, "normal"))
  
