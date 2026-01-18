# Basic List Operations

fruits = ["Apple","Mango","Banana"]
print(fruits)
print(fruits[0])
print(len(fruits))

# Loop through list

for fruit in fruits:
  print(fruit)


# Number Processing

numbers = [10,20,30,40,50,60]
total = 0

for number in numbers:
  total += number

print("Total:", total)
print("Average:", total/len(numbers))


# Modifying List

numbers.append(70)
numbers.remove(20)

print(numbers)
