# Handle bad input

try:
  age = int(input("Enter age: "))
  print("Age:", age)
except ValueError:
  print("Please enter a Valid number")

# File safety

try:
  with open("data.txt","r") as file:
    print(file.read())
except FileNotFoundError:
  print("data.txt not found")

# Safe data parsing

data = ["25","30","abc","40","cde"]

for item in data:
  try:
    print(int(item))
  except ValueError:
    print("Invalid number:", item)


# Combining With logic

def divde(a,b):
  try:
    return a/b
  except ZeroDivisionError:
    return "Cannot divide by zero"

print(divde(5,2))
print(divde(7,0))