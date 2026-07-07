import random
from data import data
from logoo import logo, vs, game_is_over

def trry():
  return random.choice(data)
def followers_info(person):
  return f"This is {person["name"]} who is {person["description"] } and lives in {person["country"]}"
def followerss(person):
  return person["followers"]
def name(person):
  return person["name"]

print(logo)

def compare(person1, person2):
  if followerss(person1) > followerss(person2):
    return name(person1)
  elif followerss(person1) < followerss(person2):
    return name(person2)
  else:
    print("Something went wrong")
right_person = []
person2 = trry()
while True:
  person1 = person2
  person2 = trry()
  while person2 == person1:
    person2 = trry()
  print(followers_info(person1))
  print(vs)
  print(followers_info(person2))
  choice = input("Who is more popular? Write (p1 or p2): ").lower()
  if choice == "p1":
    if name(person1) == compare(person1, person2):
      print("Right")
      right_person.append(person1)
      person1 = right_person
      person2 = data.pop(random.randint(0, len(data) - 1))
    elif data == name(person1):
      print("You won")
      break
    else:
      print("Game is over")
      break
  elif choice == "p2" :
    if name(person2) == compare(person1, person2):
      print("Right")
      right_person.append(person2)
      person2 = right_person
      person1 = data.pop(random.randint(0, len(data) - 1))
    elif data == name(person2):
      print("You won")
      break
    else:
      print("Game is over")
      break
  else:
    print("invalid syntax")
print(f"U had {len(right_person)} right answers")
print(game_is_over)