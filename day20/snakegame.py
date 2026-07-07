from turtle import  Screen, colormode
from random import randint
from snakebody import Snake
from food import Food
from score import Score
import time
screen = Screen()
full_snake=[]
xcor = [0, -20, -40]
screen.setup(600,600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)
screen.listen()
game_is_on = True
snake = Snake()
food = Food()
score = Score()
screen.onkey(snake.up, "w")
screen.onkey(snake.down, "s")
screen.onkey(snake.right, "a")
screen.onkey(snake.left, "d")

while game_is_on:
  screen.update()
  time.sleep(0.1)
  snake.move()
  if snake.head.distance(food) < 15:
    food.refresh(snake)
    snake.extend()
    score.increase_score()
  if snake.head.xcor()>285 or snake.head.xcor()<-285 or snake.head.ycor()>285 or snake.head.ycor()<-285:
    score.reset_score()
    snake.reset_snake()
    for segment in snake.full_snake[1:]:
      if snake.head.distance(segment) < 10:
        score.reset_score()
        snake.reset_snake()

  
    
  
  

  



  






screen.exitonclick()