import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
plt.rcParams["figure.figsize"] = (20.0, 10.0)

# Readig Data
data = pd.read_csv("headbrain.csv")
print(data.shape)
data.head()



# Collecting X and Y
X = data["Head Size(cm^3)"].values
Y = data["Brain Weight(grams)"].values



# Mean of X and Y
mean_x = np.mean(X)
mean_y = np.mean(Y)

# Total number of values
n = len(X)

# Using the formula to calculate b1 and b2
numerator = 0
denominator = 0

for i in range(n):
    numerator += (X[i] - mean_x) * (Y[i] - mean_y)
    denominator += (X[i] - mean_x) ** 2
b1 = numerator / denominator
b0 = mean_y - (b1 * mean_x)

# Print Coefficients
print(f"b1: {b1}, b0: {b0}")



# Plotting Values and Regression Line
max_x = np.max(X) + 100
min_x = np.min(X) - 100

# Calculating Line Values X and Y
x = np.linspace(min_x, max_x, 1000)
y = b0 + b1 * x

# Plotting Line
plt.plot(x, y, color="#58b970", label="Regression Line")

# Plotting Scatter Points
plt.scatter(x, y, c="#ef5423", label="Scatter Plot")

plt.xlabel("Head Size in cm3")
plt.ylabel("Brain Weight in grams")
plt.legend()
plt.show()



# Calculating the r^2 Value
ss_t = 0
ss_r = 0
for i in range(n):
    y_pred = b0 + b1 * X[i]
    ss_t += (Y[i] - mean_y) ** 2
    ss_r += (Y[i] - y_pred) ** 2
r2 = 1 - (ss_r/ss_t)
print(f"r2: {r2}")



# Implementing Linear Regression using AI -> ML
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error

# Cannot use Rank 1 Matrix in scikit learn
X = X.reshape((n, 1))

# Creating Model
reg = LinearRegression()

# Fitting Training Data
reg = reg.fit(X, Y)

# Y Prediction
Y_pred = reg.predict(X)

# Calculating RMSE and R2 Score
mse = mean_squared_error(Y, Y_pred)
rmse = np.sqrt(mse)
r2_score = reg.score(X, Y)

print(f"RMSE: {np.sqrt(mse)}")
print(f"r^2 Score: {r2_score}")