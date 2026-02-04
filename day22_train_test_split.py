import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split

# Load data
data = pd.read_csv("house_data.csv")
print(data)

# Seperate X and y
X = data[["bedrooms","bathrooms","area_sqft"]]
y = data["price"]

# Split data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size= 0.4, random_state= 42)

# Train Model
model = LinearRegression()
model.fit(X_train, y_train)

# Test Model
predictions = model.predict(X_test)

# Check Accuracy
score = model.score(X_test, y_test)
print("Model accuracy Score:", score)

# Compare Real vs Predicted
results = pd.DataFrame({
  "Real_Price": y_test,
  "Predicted_Price":predictions
})
print("\nComparison:\n", results)