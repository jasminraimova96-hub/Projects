from turtle import Turtle, Screen, colormode
from random import randint

lia = Turtle()
screen = Screen()

colormode(255)

def rcolor():
    r = randint(0, 255)
    g = randint(0, 255)
    b = randint(0, 255)
    return (r, g, b)
lia.speed("fastest")
lia.penup()
x= - 300
y= - 250
lia.goto(x,y)
for fullpicture in range(10):
  for dot in range(11):
    lia.color(rcolor())
    lia.dot(20)
    lia.penup()
    lia.forward(60)
  y += 40
  lia.goto(x,y)
lia.hideturtle() 
screen.exitonclick()
