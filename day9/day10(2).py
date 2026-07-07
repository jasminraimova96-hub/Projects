print("Calculator")
def add(n1, n2):
  return n1 + n2
def subtract(n1, n2):
  return n1 - n2
def multiply(n1, n2):
  return n1 * n2
def divide(n1, n2):
  return n1 / n2  
sign_dict = {
  "+" : add,
  "-" : subtract,
  "*" : multiply,
  "/" : divide
}
def calculator():
  n1 = float(input("Enter first number: "))
  print(sign_dict.keys())
  while True:
    sign = input("Pick an operation: ")
    n2 = float(input("Enter next number: "))
    if sign in sign_dict:
      result = sign_dict[sign](n1,n2)
    else:
      print("Invalid operator!")
      continue
    again = input(f"Type 'y' to continue calculating with {result}, or type 'n' to start a new calculation: ").lower()
    if again == "y":
      n1 = result
    elif again == "n":
      n1 = n1
    else:
      return result
result = calculator()
print(result)
  


