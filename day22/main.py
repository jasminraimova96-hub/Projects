from turtle import  Screen
from paddle import Paddle
from ball import Ball
from score import Score
import time 
screen = Screen()
screen.setup(800,600)
screen.bgcolor("black")
screen.title("Pong")
screen.listen()
screen.tracer(0)
r_paddle = Paddle((350, 0))
l_paddle = Paddle((-360, 0))  
ball = Ball()
screen.onkey(r_paddle.up,"w")
screen.onkey(r_paddle.down,"s")
screen.onkey(l_paddle.up,"Up")
screen.onkey(l_paddle.down,"Down")
r_score = Score((-30,260))
l_score = Score((30,260))
game_on = True
while game_on:
  screen.update()
  time.sleep(ball.move_speed)
  ball.move()
  if ball.ycor() > 280 or ball.ycor() < -280:
    ball.bounce_y()
  if ball.distance(r_paddle) < 50 and ball.xcor() > 320:
    ball.bounce_x()
  elif ball.distance(l_paddle) < 50 and ball.xcor() < -320:
    ball.bounce_x()
  if ball.xcor() > 390:
    l_score.increase_score()
    ball.reset_position()
  if ball.xcor() < -390:
    r_score.increase_score()
    ball.reset_position() 

screen.exitonclick()