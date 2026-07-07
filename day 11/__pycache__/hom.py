import json
name = input("Enter name: ")
age = input("Enter age: ")
data = {"name": name, "age": age}
with open("user.json", "w") as f:
    json.dump(data, f)
with open("user.json", "r") as f:
    saved = json.load(f)
print("Saved data:", saved)