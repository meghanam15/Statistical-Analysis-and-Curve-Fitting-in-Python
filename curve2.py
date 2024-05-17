import numpy as np
import matplotlib.pyplot as plt
from tabulate import tabulate
# Define the function to fit (a curve of the form y = ax^b)
def power_curve(x, a, b):
    return a * np.power(x, b)

n = int(input("Enter the number of data points: "))
# Get data from the user
x_input = input("Enter x values separated by comma: ")
y_input = input("Enter y values separated by comma: ")

x_data = np.array([float(x) for x in x_input.split(",")])
y_data = np.array([float(y) for y in y_input.split(",")])

data = [[x_data[i], y_data[i]] for i in range(n)]
print(tabulate(data, headers=["X", "Y"], tablefmt="pretty"))

# Perform linear regression
# Linearize the model: log(y) = log(a) + b * log(x)
log_x_data = np.log(x_data)
log_y_data = np.log(y_data)

# Perform linear regression manually
n = len(log_x_data)
sum_x = np.sum(log_x_data)
sum_y = np.sum(log_y_data)
sum_x_squared = np.sum(log_x_data ** 2)
sum_xy = np.sum(log_x_data * log_y_data)

# Calculate coefficients
b = (n * sum_xy - sum_x * sum_y) / (n * sum_x_squared - sum_x ** 2)
a = np.exp((sum_y - b * sum_x) / n)

# Generate points for plotting the fitted curve
x_fit = np.linspace(min(x_data), max(x_data), 100)
y_fit = power_curve(x_fit, a, b)

print("Fitted coefficients:")
print("a =", a)
print("b =", b)
print("Fitted equation:")
print(f"y = {a:.2f} * x^{b:.2f}")

# Plot the original data and the fitted curve
plt.scatter(x_data, y_data, label='Data')
plt.plot(x_fit, y_fit, color='red', label='Fitted Curve')
plt.xlabel('X')
plt.ylabel('Y')
plt.legend()
plt.grid(True)
plt.title('Fitting a Power Curve (y = ax^b) to User Data')
plt.show()
