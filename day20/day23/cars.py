from turtle import Turtle
from random import randint, choice
COLORS = ["red", "yellow", "orange", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10
class Cars(Turtle):
  def __init__(self):
    super().__init__()
    self.cars = []
    self.cars_speed = STARTING_MOVE_DISTANCE
    self.hideturtle()
  def create_cars(self):
    random_cahnce = randint(1, 6)
    if random_cahnce == 1:
      new_car = Turtle("square")
      new_car.penup()
      new_car.color(choice(COLORS))
      new_car.shapesize(stretch_wid=1, stretch_len=2)
      random_y = randint(-250,250)
      new_car.goto(300, random_y)
      self.cars.append(new_car)
    
  def move(self):
    for cars in self.cars:
      cars.backward(self.cars_speed )
  def level_up(self):
    self.cars_speed +=  MOVE_INCREMENT

