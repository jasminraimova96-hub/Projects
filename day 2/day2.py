print("Hello!")
'''
bill = float(input("What was the total bill? $"))
percentage = float(input("What % tip would you like to give? 10 12 15: "))
people = int(input("How many people to split the bill? "))
bill_w = percentage / 100 * bill + bill
total_person = bill_w/people
a = round(total_person, 2)
print(a)
''' '''
a = input("Choose right or left: ").lower()
if a == "left":
  print("Next step")
  b = input("Choose between colors - yellow, pink, red: ").lower()
  if b == "pink":
    print("U win")
  else:
    print("game is over")
else:
  print("game is over")
'''
fruits = ["Strawberries", "Nectarines", "Apples", "Grapes", "Peaches", "Cherries", "Pears"]
vegetables = ["Spinach", "Kale", "Tomatoes", "Celery", "Potatoes"]
 
dirty_dozen = [fruits, vegetables]
 
print(dirty_dozen[1][1])