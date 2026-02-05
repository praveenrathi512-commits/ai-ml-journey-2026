import pandas as pd
from sklearn.linear_model import LinearRegression

# Load & Train Data
data = pd.read_csv("house_data.csv")

X = data[["bedrooms", "bathrooms", "area_sqft"]]
y = data["price"]

model = LinearRegression()
model.fit(X, y)

# Cofficients
print("Intercept (base price):", model.intercept_)
print("Feature cofficients:")

for feature, coef in zip(X.columns, model.coef_):
  print(f"{feature} -> {coef}")

# Predict and explain
new_house = [[4,2,1750]]
pred = model.predict(new_house)[0]

print("\nPrediction for house:", pred)
print("\nBreakdown of prediction")

for feature, coef, value in zip(X.columns, model.coef_, new_house[0]):
  print(f"{feature}: {value} * {coef} = {value * coef}")

print("Base price (intercept):", model.intercept_)
