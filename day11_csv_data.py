# Read and print rows

import csv

with open("people.csv",newline= '') as file:
  reader = csv.reader(file)
  for row in reader:
    print(row[0])

# Skip Header and format outpur

with open("people.csv",newline='') as file:
  reader = csv.reader(file)
  next(reader)

  for row in reader:
    name, age, city = row
    print(f'{name} is {age} years old and lives in {city}')

# Calculate average age

total_age = 0
count = 0

with open("people.csv",newline='') as file:
  reader = csv.reader(file)
  next(reader)
  
  for row in reader:
    total_age += int(row[1])
    count += 1

print("Average age:", total_age/count)

# Save filtered data

with open("filtered.csv", "w", newline='') as file_out:
  writer = csv.writer(file_out)
  writer.writerow(["name","age","city"])

  with open("people.csv",newline='') as file:
    reader = csv.reader(file)
    next(reader)
    
    for row in reader:
      if (int(row[1]) >= 25):
        writer.writerow(row)
  
