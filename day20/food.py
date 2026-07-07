from turtle import Turtle, Screen, colormode
from random import randint
from snakebody import Snake 
class Food(Turtle):
  def __init__(self):
    super().__init__()
    self.shape("circle")
    self.penup()
    self.shapesize(0.5,0.5)
    self.color(self.rcolor())
    self.speed("fastest")
    self.goto(randint(-280,280), randint(-280,280))
  def refresh(self,snake):
    valid_position = False
    while not valid_position:
      self.goto(randint(-280,280),randint(-280,280))
      self.color(self.rcolor())
      valid_position = True
      for segment in snake.full_snake:
        if self.distance(segment) < 10:
          valid_position = False
  colormode(255)

  def rcolor(self):
    r = randint(0, 255)
    g = randint(0, 255)
    b = randint(0, 255)
    return (r, g, b)