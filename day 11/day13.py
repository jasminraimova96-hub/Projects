import random
from guess import logo
print(logo)
def r_number():
  return random.randint(1,100)
s_number = r_number()
print("Welcome to the number printing game!")
def game():
  print("You will have to guess the number between 1 and 100")
  level = input("Choose the leve hard ('h') or easy ('e'): ")
  if level == "h":
    attempts = 5
  elif level == "e": 
    attempts = 10
  else:
    print("invalid syntax")
  while attempts > 0:
    guess = int(input("Enter your guess: "))
    if guess == s_number:
      print("U won")
      break
    elif guess > s_number:
      print("Wrong number, too high!")
      attempts -= 1
      print("Attempts left:", attempts)
    elif guess < s_number:
      print("Wrong number, too low!")
      attempts -= 1
      print("Attempts left:", attempts)
    else:
      print("Invalid syntax")
      break
    if attempts == 0:
        print("Game over! The number was", s_number) 
        break
game()
while input("Do you want to play again print 'y' if yes and 'n' if no: ") == "y":
  game()


