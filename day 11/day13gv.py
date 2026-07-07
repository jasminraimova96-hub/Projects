import random
from guess import logo
print(logo)
EASY_LEVEL = 10
HARD_LEVEL = 5
answer = random.randint(1,100)
def set_difficulty():
  level = input("Choose the leve hard ('h') or easy ('e'): ")
  if level == "h":
      return HARD_LEVEL
  elif level == "e":
      return EASY_LEVEL 
def check_answer(user_guess, actual_number, turns):
  if actual_number == user_guess:
    print(f"You won")
  elif user_guess < actual_number:
    print(f"Too low, try again, you have {turns-1}")
    return turns - 1
  elif user_guess > actual_number:
    print(f"Too high, try again, you have {turns-1}")
    return turns - 1
  else:
    return f"Game is over, you have {turns} left"
def game():
  print("Welcome to the number printing game!")
  guess = 0
  turns = set_difficulty()
  while guess != answer:
    guess = int(input("Enter your number: "))
    turns = check_answer(guess, answer, turns)
    if turns == 0:
      print(f"Game is over, guess number was {answer}")
      return
    elif guess != answer:
      print("Guess again")
game()
while input("Do you want to play again print 'y' if yes and 'n' if no: ") == "y":
  game()