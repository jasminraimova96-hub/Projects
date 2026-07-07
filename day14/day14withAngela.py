import random
from data import data
from logoo import logo, vs, game_is_over
score = 0
def format_data(account):
  account_name = account["name"]
  account_desc = account["description"]
  account_city = account["country"]
  return f"{account_name}, a {account_desc}, from {account_city}"
def check_answer(guess, account_a, account_b):
  if account_a > account_b:
    return guess == "a"
  else:
    return guess == "b"
account_c = random.choice(data)
while True: 
  account_a = account_c
  account_b = random.choice(data)
  if account_a == account_b:
    account_b = random.choice(data)
  print(logo)
  print(f"Compare A:{format_data(account_a)}")
  print(vs)
  print(f"Against B:{format_data(account_b)}")
  guess = input("Who has more followers A or B: ").lower()
  a_follower = account_a["followers"]
  b_follower = account_b["followers"]
  is_correct = check_answer(guess, a_follower, b_follower)
  if is_correct:
    score += 1
    print(f"You are right! Current score {score}")
  else:
    print(f"Sorry, that's wrong! Your final score is {score}")
    break