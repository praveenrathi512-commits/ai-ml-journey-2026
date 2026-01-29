import numpy as np
from sklearn.linear_model import LinearRegression

# Prepare Dataset

# X = Experience Years
X = np.array([1,2,3,4,5,6]).reshape(-1,1)

# y = Salary (LPA)
y = np.array([3,4,6,8,10,13])

print("Training Data:")
print("Experience (X):\n", X)
print("Salary (y):", y)

# Create Model

model = LinearRegression()

# Train Model

model.fit(X, y)
print("\nModel trained sucessfully")

# Learned Parameters

print("\nLearned slope (m):", model.coef_)
print("Learned intercept (b):", model.intercept_)

# Make Predictions

new_experience = [[7]]
predicted_salary = model.predict(new_experience)
print("\nPredictions:")
print(f"Experience: {new_experience[0][0]} years")
print(f"Predicted Salary: {predicted_salary[0]:.2f} LPA")
