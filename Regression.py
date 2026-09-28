# Experiment 1: Regression Model for House Price Prediction

import numpy as np
import matplotlib.pyplot as plt

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score

# Dataset
# Area in square feet
X = np.array([
    800, 1000, 1200, 1500, 1800,
    2000, 2200, 2500, 2800, 3000
]).reshape(-1, 1)

# House price in Lakhs
y = np.array([
    40, 50, 60, 75, 90,
    100, 110, 125, 140, 150
])

# Split data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Create Linear Regression model
model = LinearRegression()

# Train model
model.fit(X_train, y_train)

# Prediction
y_pred = model.predict(X_test)

# Evaluation metrics
mae = mean_absolute_error(y_test, y_pred)
mse = mean_squared_error(y_test, y_pred)
rmse = np.sqrt(mse)
r2 = r2_score(y_test, y_pred)

print("----- Linear Regression Results -----")
print("Slope:", model.coef_[0])
print("Intercept:", model.intercept_)

print("\nEvaluation Metrics:")
print("MAE  :", mae)
print("MSE  :", mse)
print("RMSE :", rmse)
print("R2   :", r2)

# Predict price for a new house
area = np.array([[2300]])
predicted_price = model.predict(area)

print("\nPredicted price for 2300 sq.ft house:",
      predicted_price[0], "Lakhs")

# Visualization
plt.scatter(X, y, color="blue", label="Actual Data")
plt.plot(X, model.predict(X), color="red", label="Regression Line")

plt.xlabel("House Area (sq.ft)")
plt.ylabel("Price (Lakhs)")
plt.title("House Price Prediction using Linear Regression")
plt.legend()
plt.show()
