from turtle import Turtle
class Lia(Turtle):
  def __init__(self):
    super().__init__()
    self.penup()
    self.goto(0,-270)
    self.shape("turtle")
    self.color("blue")
    self.setheading(90)
    self.shapesize(stretch_wid=0.8, stretch_len=0.8)
  def up(self):
    self.sety(self.ycor() + 20)
  def down(self):
    self.sety(self.ycor() - 20)
  def right(self):
    self.setx(self.xcor() - 20)
  def left(self):
    self.setx(self.xcor() + 20)