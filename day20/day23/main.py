from turtle import Screen 
from liaturtle import Lia
from cars import Cars
from score import Score
import time
screen = Screen()
screen.setup(800,600)
screen.listen()
screen.tracer(0)
turtle = Lia()
carss = Cars()
score = Score()
carss.create_cars()
screen.onkey(turtle.up,"w")
screen.onkey(turtle.down,"s")
screen.onkey(turtle.right,"a")
screen.onkey(turtle.left,"d")
game_on = True
while game_on:
  time.sleep(0.1)
  screen.update()
  carss.create_cars()
  carss.move()
  for car in carss.cars:
    if car.distance(turtle) < 20:
      game_on = False
      score.game_over()
  if turtle.ycor() > 270:
    turtle.goto(0, -270)
    carss.level_up()
    score.increase_score()
  
screen.exitonclick()