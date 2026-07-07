from turtle import Turtle
STARTING_POSITION = [(0,0), (-20,0), (-40,0)]
class Snake:
  def  __init__(self):
    self.full_snake=[]
    self.create_snake()
    self.head = self.full_snake[0]
  def create_snake(self):
    for position in STARTING_POSITION:
      self.add_segment(position)
  def up(self):
    if self.head.heading() != 270:
      self.head.setheading(90)
  def down(self):
    if self.head.heading() != 90:
      self.head.setheading(270)
  def right(self):
    if self.head.heading() != 0:
      self.head.setheading(180)
  def left(self):
    if self.head.heading() != 180:
      self.head.setheading(0)
  def add_segment(self,position):
    li = Turtle("square")
    li.color("white")
    li.penup()
    li.goto(position)
    self.full_snake.append(li)
  def extend(self):
    self.add_segment(self.full_snake[-1].position())
  def move(self):
    for snake_position in range(len(self.full_snake)-1,0,-1):
      new_x = self.full_snake[snake_position - 1].xcor()
      new_y = self.full_snake[snake_position - 1].ycor()
      self.full_snake[snake_position].goto(new_x,new_y)
    self.full_snake[0].forward(20)
  def reset_snake(self):
    for seg in self.full_snake:
      seg.goto(100000,100000)
    self.full_snake.clear()
    self.create_snake()
    self.head = self.full_snake[0]

      
