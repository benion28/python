# Libraries
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
# %matplotlib inline
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
from sklearn.metrics import mean_absolute_error
from sklearn.model_selection import train_test_split
# from sklearn.externals import joblib



# Readig Data
data = pd.read_csv("C:\\Benion\\Benion Programmings\\Python\\AI & ML\\data\\tree-diameter-height.csv")
data.shape



data.head(10)



# Number of parameters in the original dataset
print(f"No of Parameters: {len(data.index)}")



# The Height distribution of the parameters
data["Height"].plot.hist()



# The Diameter distribution of the parameters
data["Diameter"].plot.hist()



data.plot(x="Height", y="Diameter", style="o")
plt.title("Height vs Diameter")
plt.xlabel("Height")
plt.ylabel("Diameter")
plt.show()


# Declaring Dependent and Independent Variables
X = data["Height"].values.reshape(-1, 1)
y = data["Diameter"].values.reshape(-1, 1)



# Data Splitting
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0)



# Fit Data into our model
model = LinearRegression()
model.fit(X_train, y_train)
# joblib.dump(model, "C:\\Benion\\Benion Programmings\\Python\\AI & ML\\data\\height-diameter.joblib")
# model = joblib.load("C:\\Benion\\Benion Programmings\\Python\\AI & ML\\data\\height-diameter.joblib")
intercept = model.intercept_[0]
slope = model.coef_[0][0]
print(f"Intercept: {intercept}")
print(f"Slope: {slope}")



# Make Prediction
predictions = model.predict(X_test)



# Compare the actual value and the predicted values
data_frame = pd.DataFrame({"Actual(x)": X_test.flatten(), "Actual(y)": y_test.flatten(), "Predicted(y)": predictions.flatten()})
data_frame



# Bar Graph
y_frame = pd.DataFrame({"Actual(y)": y_test.flatten(), "Predicted(y)": predictions.flatten()})
data_frame_graph = y_frame.head(25)
data_frame_graph.plot(kind="bar", figsize=(16, 10))
plt.grid(which="major", linestyle="-", linewidth="0.5", color="green")
plt.grid(which="minor", linestyle=":", linewidth="0.5", color="black")
plt.show()



# A Straight Line Plot
plt.scatter(X_test, y_test, color="gray")
plt.plot(X_test, predictions, color="red", linewidth=2)
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
regression_model = LinearRegression()
regression_model.fit(X, y)
# regression_model = joblib.load("C:\\Benion\\Benion Programmings\\Python\\AI & ML\\data\\manual-height-diameter.joblib")
X_predict = [[14.543234]]
y_predict = regression_model.predict(X_predict)
predicted_value = y_predict[0][0]
print(f"Predicted Diameter(y): {predicted_value}")