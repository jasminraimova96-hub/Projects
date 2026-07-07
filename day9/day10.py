print("Calculator")
def calculator():
  f_number = float(input("Enter first number: "))
  print("+\n-\n/\n*")
  while True: 
    sign = input("Pick an operation: ")
    s_number = float(input("Enter next number: "))
    if sign == "+":
      return f_number + s_number
    elif sign == "-":
      return f_number - s_number
    elif sign == "*":
      return f_number * s_number
    elif sign == "/":
      return f_number / s_number  
    else:
      print("That operator doesn't exist.")
result = calculator()
print(result)      
while True:
  next_v = input(f"Type 'y' to continue calculating with {result}, or type 'n' to start a new calculation: ").lower()
  if next_v == "y":
   sign = input("Pick an operation: ")
   s_number = float(input("Enter next number: "))
   if sign == "+":
    result = result + s_number
   elif sign == "-":
      result = result - s_number
   elif sign == "*":
    result = result * s_number
   elif sign == "/":
    result = result / s_number  
   else:
    print("That operator doesn't exist!")
   print(result)
  elif next_v == "n":
    result = calculator()
    print(result)  
  elif next_v == "n":
    result = calculator()
    print(result)  
  else:
    esc = input("Do u want to escape?(yes/n0):").lower()
    if esc != "yes":
      print("Input was invalid")
    else:
      print("End!")
    

  
