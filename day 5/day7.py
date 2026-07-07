import random
word = ["apple", "lion", "banana"]
print(word)
guess = random.choice(word)
display = ['_'] * len(guess)
while '_' in display:
    print("\nCurrent word:", display)
    letter = input("Enter letter: ").lower()
    if letter in guess:
        for l in range(len(guess)):
            if guess[l] == letter:
                display[l] = letter
        print("Correct letter")
    else:
        print("Wrong letter")

print("\nYou guessed the word:", guess)
      


    

