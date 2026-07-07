print('Hello')
alphabet = "abcdefghijklmnopqrstuvwxyz"
while True:
  tryy = input("Do u want to use Caeser cipher (yes/no): ")  
  if tryy == "yes":
    s_word = input("Enter your word: ").lower()
    shift = int(input("Type the shift number: "))
    def ceaser(s_word, shift):.
      decode = input("Do u want to 'decode' or 'encode' secret word): ").lower()
      word = ""
      local_shift = shift
      if decode == "decode":
        local_shift *= -1
      for letter in s_word:
        if letter in alphabet:  
          position = alphabet.index(letter)
          new_position = (position + local_shift) % len(alphabet)
          new_letter = alphabet[new_position]
          word += new_letter
        else:
          word += letter
      print(word)
    ceaser(s_word, shift)
  elif tryy == "no":
      print("Bye!")
      break
  else:
      print("Invalid syntax")




