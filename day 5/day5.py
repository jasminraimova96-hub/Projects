import random
letters = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
numbers = ['0','1','2','3', '4', '5', '6', '7', '8','9']
symbols = ['!','@','$', '%', '^', '&', '*','(', ')', '_']
print('Welcome to password generator ')
nl = random.randint(8,10)
nn = random.randint(2, 4)
ns = random.randint(2,4)
password_l = []
for char in range(0,nl):
  password_l.append(random.choice(letters))
 
for char in range(0,nn):
  password_l.append(random.choice(numbers))
 
for char in range(0,ns):
  password_l.append(random.choice(symbols))
random.shuffle(password_l)

password = ""
for char in password_l:
  password += char
print(password)