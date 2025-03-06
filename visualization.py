# visualization.py
import matplotlib.pyplot as plt

def plotRegression(X, y, y_pred, title="Regression Plot", x_label="X", y_label="y"):
   
    plt.scatter(X, y, color='blue', label='Actual Data')
    plt.plot(X, y_pred, color='red', label='Predicted Data')
    plt.xlabel(x_label)
    plt.ylabel(y_label)
    plt.title(title)
    plt.legend()
    plt.show()