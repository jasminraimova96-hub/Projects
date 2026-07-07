import pandas
data = pandas.read_csv(r"C:\Users\User\Desktop\100 days\day26\day 26\npa.csv")
words_data_frame = pandas.DataFrame(data)
dictt = {row.letter: row.code for (index, row) in words_data_frame.iterrows()} 
def generate_p():
  user_input = input("Enter a word: ").upper()
  try: 
    letters_in_user_input = [dictt[letter] for letter in user_input]
  except KeyError:
    print("You can enter only letters")
    generate_p()
  else:
    print(letters_in_user_input)
generate_p()
    