# Read full file

with open("data.txt", "r") as file:
    content = file.read()
print(content)

# Read file line by line

with open("data.txt","r") as file:
    for line in file:
        name, age, city = line.split(",")
        print(name,age,city)


# Writing processed data

with open("processed.txt","w") as file:
    file.write("Name | Age | City\n")

    with open("data.txt", "r") as data:
        for line in data:
            name, age, city = line.split(",")
            file.write(f"{name} | {age} | {city}\n")


# Simple analytics

total_age = 0
count = 0

with open("data.txt","r") as file:
    for line in file:
        _,age,_ = line.split(",")
        total_age += int(age)
        count += 1

print("Average age",total_age/count)