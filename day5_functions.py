# Function Example

def greet():
  print("Hello!")

greet()


# Function with Parameters

def greet(name):
  print("Hello",name)

greet("Jack")


# Function that returns value (adding two numbers)

def add(a, b):
    return a + b

result = add(5, 7)
print("Sum:", result)

# Calculate Average

def calculate_average(numbers):
    total = 0
    for number in numbers:
      total += number
    return total/len(numbers)

marks = [50,55,75,85]
avg = calculate_average(marks)
print("Average:", avg)

# Grade Funtion

def get_grade(marks):
   if marks >= 92:
      return "A"
   elif marks >= 75:
      return "B"
   elif marks >= 60:
      return "C"
   else:
      return "Fail"

print(get_grade(83))