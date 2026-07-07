from turtle import Turtle, Screen
from random import randint,choice
screen = Screen()
screen.setup(500, 400)
is_race_on = False
user_bet = screen.textinput(
    title="Make your bet",
    prompt="Which turtle will win the race? Enter a color: "
).lower()
print(user_bet)
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
all_turtles = []
y = [-70, -40, -10, 20, 50, 80]
for turtle in range(0,6):
  li = Turtle("turtle")
  li.penup()
  li.color(colors[turtle])
  li.goto(-230, y[turtle])
  all_turtles.append(li)
  
if user_bet:
  is_race_on = True
while is_race_on:
  for turtle in all_turtles:
    if turtle.xcor()> 230:
      is_race_on = False
      winning_color = turtle.pencolor()
      if winning_color == user_bet:
        print(f"Your turtle {winning_color} won!")
        break
      else:
        print(f"You have lost! turtle {winning_color} won!")
        break
    distance = randint(0,10)
    turtle.forward(distance)  
screen.exitonclick()