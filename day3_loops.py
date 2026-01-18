# Print Numbers

for i in range(1,11):
  print(i)

# Sum of Numbers

total = 0
for i in range(1,11):
  total += i
print(total)

# Even Numbers

for i in range(1,11):
  if i%2 == 0:
    print(i,"is even number")

# While Loop Practice

num = 5
while num > 0:
  print(num)
  num -= 1
print("Done")

# Factorial of Number

n = 8
fact = 1
for i in range(n,1,-1):
  fact *= i
print(fact)