'''from turtle import Turtle, Screen
timmy = Turtle()
timmy.shape("turtle")
for steps in range(100):
  for c in ('DeepPink3', 'DeepPink4', 'DeepPink1'):
    timmy.color(c)
    timmy.forward(steps)
    timmy.right(30)

print(timmy)
my_screen = Screen()
print(my_screen.canvheight)
my_screen.exitonclick()'''
from prettytable import PrettyTable
table = PrettyTable()
table.add_column("Pokemon name: ", ["Chespin", "Vivillon", "Beedrill"])
table.add_column("Type: ", ["Grass", "Bug/Flying", "Bug/Poison"])
table.align = "l"
print(table)