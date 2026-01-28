import matplotlib.pyplot as plt

# Line PLot - Trend

years = [1,2,3,4,5]
skill_level = [2,4,6,8,10]

plt.plot(years, skill_level)
plt.title("Skill Growth Over Time")
plt.xlabel("Years of Practice")
plt.ylabel("Skill Level")
plt.show()

# Scatter Plot - Relationship

experience = [1,2,3,4,5,6]
salary = [3,4,6,9,11,14]
plt.scatter(experience,salary)
plt.title("Scatter Plot: Experience vs Salary")
plt.xlabel("Experience (Years)")
plt.ylabel("Salary (LPA)")
plt.show()

# Histogram - Distribution

ages = [22,23,25,26,28,32,27,24,35,34]
plt.hist(ages, bins= 5)
plt.title("Histogram: Age Distribution")
plt.xlabel("Age")
plt.ylabel("Frequency")
plt.show()