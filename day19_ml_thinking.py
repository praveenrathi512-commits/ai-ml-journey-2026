from sklearn.linear_model import LinearRegression
import numpy as np

# Simple Thinking
  # Training Data
X = np.array([1,2,3,4]).reshape(-1,1)
y = np.array([3,4,6,8])

model = LinearRegression()
model.fit(X, y)

print("Prediction for 5 years:", model.predict([[5]])[0])

# Change the Data

X = np.array([2, 4, 6, 8]).reshape(-1,1)
y = np.array([5, 9, 13, 17])

model.fit(X, y)

print("Prediction for 10 years:", model.predict([[10]])[0])

# More Example

X = np.array([1,2,3,4,5,6]).reshape(-1,1)
y = np.array([2,4,6,8,10,12])

model.fit(X, y)
print("Prediction for 7 years:", model.predict([[7]])[0])