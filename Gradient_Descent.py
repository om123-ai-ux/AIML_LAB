# Experiment 2: Gradient Descent for Linear Regression

import numpy as np
import matplotlib.pyplot as plt

# Dataset
# Area in square feet
X = np.array([
    800, 1000, 1200, 1500, 1800,
    2000, 2200, 2500, 2800, 3000
], dtype=float)

# Price in Lakhs
y = np.array([
    40, 50, 60, 75, 90,
    100, 110, 125, 140, 150
], dtype=float)

# Normalize X for better gradient descent performance
X_mean = np.mean(X)
X_std = np.std(X)

X_scaled = (X - X_mean) / X_std

# Initialize parameters
w = 0.0
b = 0.0

# Hyperparameters
learning_rate = 0.01
epochs = 1000

n = len(X)

loss_history = []

# Gradient Descent
for epoch in range(epochs):

    # Prediction
    y_pred = w * X_scaled + b

    # Calculate error
    error = y_pred - y

    # Calculate gradients
    dw = (2 / n) * np.sum(X_scaled * error)
    db = (2 / n) * np.sum(error)

    # Update parameters
    w = w - learning_rate * dw
    b = b - learning_rate * db

    # Calculate MSE
    mse = np.mean(error ** 2)

    loss_history.append(mse)

# Final predictions
y_pred = w * X_scaled + b

# Evaluation metrics
mae = np.mean(np.abs(y - y_pred))
mse = np.mean((y - y_pred) ** 2)
rmse = np.sqrt(mse)

ss_total = np.sum((y - np.mean(y)) ** 2)
ss_residual = np.sum((y - y_pred) ** 2)

r2 = 1 - (ss_residual / ss_total)

print("----- Gradient Descent Results -----")

print("Weight (w):", w)
print("Bias (b):", b)

print("\nEvaluation Metrics:")
print("MAE  :", mae)
print("MSE  :", mse)
print("RMSE :", rmse)
print("R2   :", r2)

# Predict price for a new house
area = 2300

area_scaled = (area - X_mean) / X_std

predicted_price = w * area_scaled + b

print("\nPredicted price for 2300 sq.ft house:",
      predicted_price, "Lakhs")

# Plot actual vs regression line
plt.scatter(X, y, color="blue", label="Actual Data")

# Sort X for proper line
sorted_indices = np.argsort(X)

plt.plot(
    X[sorted_indices],
    y_pred[sorted_indices],
    color="red",
    label="Gradient Descent Regression"
)

plt.xlabel("House Area (sq.ft)")
plt.ylabel("Price (Lakhs)")
plt.title("Linear Regression using Gradient Descent")
plt.legend()
plt.show()

# Plot loss function
plt.plot(loss_history)

plt.xlabel("Epoch")
plt.ylabel("MSE Loss")
plt.title("Gradient Descent Convergence")

plt.show()
