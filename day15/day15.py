from ingridients import menu,resources
profit = 0
storage = resources
def coffe_machine():
  def coins():
    global profit
    total = int(input("How many quarters?: "))* 0.25 
    total += int(input("How many dimes?: "))* 0.10
    total += int(input("How many nickels?: "))* 0.05
    total += int(input("How many pennies?: "))* 0.01
    if menu[u_input]["cost"] <= total:
      profit += total
      for item in menu[u_input]["ingredients"]:
        storage[item] -= menu[u_input]["ingredients"][item]
      print("Here is your coffee ☕")
    else:
      print("Sorry, not enough money.")    
  want = input("menu: \n 1)Buy a coffee?(1) \n 2)Check Resourses(2) \n 3)Check proffit(3) \n ")
  if want == "1":
    u_input = input("What would you like? (espresso/latte/cappuccino):").lower()
    print(f"{u_input} costs {menu[u_input]["cost"]}")
    print(coins())
  elif want == "2":
    print(storage)
  elif want == "3":
    print(profit) 
  else:
    print("You should choose in numbers (1/2/3)")
print(coffe_machine())
while input("Do you want to go back to menu? ('yes'/'no'): ").lower() == "yes":
  print(coffe_machine())


