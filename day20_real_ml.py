import pandas as pd
from sklearn.linear_model import LinearRegression

# Load CSV 
data = pd.read_csv("salary_data.csv")
print("Dataset:\n", data)

# Seperate X and y
X = data[["experience"]] # feature (input)
y = data["salary"] # label (output)

# Train Model
model = LinearRegression()
model.fit(X, y)

# Predict new value
prediction = model.predict([[8]])
print("Predicted salary for 8 years:", prediction[0])

prediction = model.predict([[9]])
print("Predicted salary for 9 years:", prediction[0])

prediction = model.predict([[10]])
print("Predicted salary for 10 years:", prediction[0])

prediction = model.predict([[15]])
print("Predicted salary for 15 years:", prediction[0])