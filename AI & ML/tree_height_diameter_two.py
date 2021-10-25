# Libraries
import pandas as pd
import numpy as np
import seaborn as sns
import math
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.svm import SVR
from sklearn.metrics import mean_squared_error
from sklearn.metrics import mean_absolute_error
from sklearn.model_selection import train_test_split
# import joblib
from random import randrange



# Readig Data
data = pd.read_csv("C:\\Benion\\Benion Programmings\\Python\\AI & ML\\data\\tree-diameter-height.csv")
data.shape



data.head(10)



# Declaring Dependent and Independent Variables
X = data["Height"].values.reshape(-1, 1)
y = data["Diameter"].values.reshape(-1, 1)

# Data Splitting
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0)

# Implement the Support Vector Machine --> Support Vector Regressor and fit the data
model = SVR(kernel="rbf")
model.fit(X_train, y_train)

# Make Prediction
predictions = model.predict(X_test)



data_frame = pd.DataFrame({"Actual(x)": X_test.flatten(), "Actual(y)": y_test.flatten(), "Predicted(y)": predictions.flatten()})
data_frame



# Bar Graph
data_frame = pd.DataFrame({"Actual(y)": y_test.flatten(), "Predicted(y)": predictions.flatten()})
data_frame_graph = data_frame.head(25)
data_frame_graph.plot(kind="bar", figsize=(16, 10))
plt.grid(which="major", linestyle="-", linewidth="0.5", color="green")
plt.grid(which="minor", linestyle=":", linewidth="0.5", color="black")
plt.show()



# Errors
mean_absolute_error = mean_absolute_error(y_test, predictions)
mean_squared_error = mean_squared_error(y_test, predictions)
root_mean_squared_error = np.sqrt(mean_squared_error)
r2_score = model.score(X_train, y_train)
print(f"Mean Absolute Error: {mean_absolute_error}")
print(f"Mean Squared Error: {mean_squared_error}")
print(f"Root Mean Squared Error: {root_mean_squared_error}")
print(f"r^2 Score: {r2_score} -- ({r2_score * 100})%")



# Make Predictions Manually
regressor_model = SVR(kernel="rbf")
regressor_model.fit(X, y)
X_predict = [[14.543234]]
y_predict = regressor_model.predict(X_predict)
predicted_value = y_predict[0]
print(f"Predicted Diameter(y): {predicted_value}")
