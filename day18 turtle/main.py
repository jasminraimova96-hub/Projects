from turtle import Turtle, Screen, colormode
from random import randint

li = Turtle()
screen = Screen()
def moveforward():
    li.forward(10)
def movebackwards():
    li.backward(10)
def counterclockwise():
    li.left(10)
def clockwise():
    li.right(10)
def clear():
    li.clear()
    li.penup()
    li.home()
    li.pendown()
screen.listen()
screen.onkey(key = "w",fun = moveforward)
screen.onkey(key = "s",fun = movebackwards)
screen.onkey(key = "a",fun = counterclockwise)
screen.onkey(key = "d",fun = clockwise)
screen.onkey(clear, "c")
screen.exitonclick()