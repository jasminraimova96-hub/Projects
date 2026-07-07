auction = {}
while True:
  name = input("Enter youjr name: ")
  value =int(input("Enter your bet: "))
  auction[name] = value 
  while True:
    new_players = input("Are there any players? (yes/no): ")
    if new_players == "yes":
      print("\n"*10)
      name = input("Enter your name: ")
      value =int(input("Enter your bet: "))
      auction[name] = value 
    else:
      break
  highest = max(auction.values())
  print(f"The highest bet was {highest}")
  print(auction)
  break
 