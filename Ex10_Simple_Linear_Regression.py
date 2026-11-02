# Ex 10: Simple Linear Regression
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score

# Dataset: Hours studied vs Marks
np.random.seed(0)
hours = np.random.uniform(1, 10, 60)
marks = 30 + 6.5 * hours + np.random.normal(0, 4, 60)
df = pd.DataFrame({"Hours": hours, "Marks": marks})
print(df.head())

X = df[["Hours"]]
y = df["Marks"]
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train model
model = LinearRegression()
model.fit(X_train, y_train)
print("\nIntercept (b0):", round(model.intercept_, 3))
print("Slope (b1):", round(model.coef_[0], 3))
print(f"Equation: Marks = {model.intercept_:.2f} + {model.coef_[0]:.2f} * Hours")

# Evaluate
y_pred = model.predict(X_test)
print("\nMAE :", round(mean_absolute_error(y_test, y_pred), 3))
print("MSE :", round(mean_squared_error(y_test, y_pred), 3))
print("RMSE:", round(np.sqrt(mean_squared_error(y_test, y_pred)), 3))
print("R2  :", round(r2_score(y_test, y_pred), 3))

# Predict new value
new = pd.DataFrame({"Hours": [7.5]})
print("\nPredicted marks for 7.5 hours:", round(model.predict(new)[0], 2))

# Plot
plt.figure(figsize=(8, 5))
plt.scatter(X_train, y_train, color="blue", label="Train")
plt.scatter(X_test, y_test, color="green", label="Test")
plt.plot(X, model.predict(X), color="red", label="Regression line")
plt.xlabel("Hours Studied"); plt.ylabel("Marks")
plt.title("Simple Linear Regression")
plt.legend(); plt.grid(True)
plt.savefig("regression.png")
plt.show()

# Residual plot
plt.figure(figsize=(8, 4))
plt.scatter(y_pred, y_test - y_pred)
plt.axhline(0, color="red")
plt.xlabel("Predicted"); plt.ylabel("Residual"); plt.title("Residual Plot")
plt.show()
