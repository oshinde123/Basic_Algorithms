import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
from visualization import plotRegression

# Sample data
X = np.array([[1], [2], [3], [4], [5]])
y = np.array([1.5, 3.5, 3.0, 4.5, 6.0])

# Split data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Create and train the model
model = LinearRegression()
model.fit(X_train, y_train)

# Make predictions using ALL of X
y_pred = model.predict(X)

# Evaluate the model on the TEST data
mse = mean_squared_error(y_test, model.predict(X_test))
print(f"Mean Squared Error: {mse}")

# Plot the results
plotRegression(X, y, y_pred, title="Linear Regression", x_label="X", y_label="y")