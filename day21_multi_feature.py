import pandas as pd
from sklearn.linear_model import LinearRegression

# Load data
data = pd.read_csv("house_data.csv")
print(data)

# Features (X) and (y)
X = data[["bedrooms", "bathrooms", "area_sqft"]]
y = data["price"]

# Train model
model = LinearRegression()
model.fit(X, y)

# Predict for a new house
new_house = [[3, 2, 1600]]
predicted_price = model.predict(new_house)

# Predict for a new house
new_house = [[5, 3, 2450]]
predicted_price = model.predict(new_house)

print("\nPredicted price for new house:", predicted_price[0], "lakhs")