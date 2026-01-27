import pandas as pd

# Create dataset
data = {
  "Name":["Amit","Riya","Kunal","Neha","Arjun"],
  "Age":[23,25,22,30,28],
  "Salary_LPA":[3,6,4,10,8]
}

df = pd.DataFrame(data)
print("\nOriginal Data:\n", df)

# Explore
print("\nInfo:\n")
print(df.info())

# Filter
high_salary = df[df["Salary_LPA"] > 5]
print("\nPeople with Salary > 5 LPA:\n", high_salary)

# Add new feature
df["Salary_in_Rupees"] = df["Salary_LPA"] * 100000
print("\nWith New Feature:\n", df)

# Prepare ML Features
X = df[["Age","Salary_in_Rupees"]]
print("\nFeature Matrix X:\n", X)

# Real World Example

raw_data = {
  "Experience_Years": [1, 3, 2, 5, 7, 4],
  "Salary_LPA": [3, 6, 4, 10, 14, 8]
}

df2 = pd.DataFrame(raw_data)
print("\nRaw Data:\n", df2)

X2 = df2[["Experience_Years", "Salary_LPA"]]

X2_norm = (X2 - X2.mean()) / X2.std()

print("\n Normalized ML-Ready Features:\n", X2_norm)
