# SUV Predictions

import numpy as np
import matplotlib as plt
import pandas as pd
%matplotlib inline



# Data Set
dataset = pd.read_csv("C:\\Benion\\Benion Programmings\\Python\\AI & ML\\data\\suv_data.csv")
dataset.head(10)



# Define our Dependent and Independent Variables
X = dataset.iloc[:, [2, 3]].values
y = dataset.iloc[:, 4].values



# Divide Dataset into Training and Testing
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25, random_state=0)



# Scale our Inputs
from sklearn.preprocessing import StandardScaler
sc = StandardScaler()
X_train = sc.fit_transform(X_train)
X_test = sc.fit_transform(X_test)



# Bring in our Logistic Regression
from sklearn.linear_model import LogisticRegression
classifier = LogisticRegression(random_state=0)
classifier.fit(X_train, y_train)



# Make Predictions
y_pred = classifier.predict(X_test)



# Calculate Accuracy
from sklearn.metrics import accuracy_score
accuracy_score(y_test, y_pred)