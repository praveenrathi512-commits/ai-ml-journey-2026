# Basic dictionary

person = {
  "name": "Jack",
  "age": 23,
  "marks":87
}

print(person["name"])
print(person["marks"])

# Student Report

student = {
  "name": "Amit",
  "marks":[79, 85, 82]
}

def calculate_average(marks):
  return sum(marks)/ len(marks)

student["average"] = calculate_average(student["marks"])

print(student)

# Loop through dictionary

for key, value in student.items():
  print(key, ":", value)


# Simple Feature Representation

house = {
  "bedrooms": 3,
  "bathrooms": 2,
  "area_sqft": 1375
}

for feature, value in house.items():
  print(feature, "=", value)