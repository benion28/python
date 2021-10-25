import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
%matplotlib inline
import math

titanic_data = pd.read_csv("C:\\Benion\\Benion Programmings\\Python\\AI & ML\\data\\titanic_dataset.csv")
titanic_data.head(10)



# Number of passengers in the original dataset
print(f"No of Passengers: {len(titanic_data.index)}")



# Analyzing Data

# Passengers who Survived VS Passengers who did not Survived
sns.countplot(x="Survived", data=titanic_data)



# Male Passengers VS Female Passengers
sns.countplot(x="Survived", hue="Sex", data=titanic_data)



# The class the Passengers were travelling in
sns.countplot(x="Survived", hue="Pclass", data=titanic_data)



# The Age distribution of the Passengers
titanic_data["Age"].plot.hist()



# The Fare of the Passengers
# The Fare of the Passengers
# titanic_data["Fare"].plot.hist(bin=20, figsize=(10, 5))
titanic_data["Fare"].plot.hist(figsize=(10, 5))



# Analyse other Columns as well (What Columns are left)
titanic_data.info()



# Siblings of the Passengers
sns.countplot(x="SibSp", data=titanic_data)



# Data Wrangling(Cleaning your Data)
sns.countplot(x="SibSp", data=titanic_data)



# Check For Values that are Null in our Data
titanic_data.isnull()



# No of Passengers with NaN Values
titanic_data.isnull().sum()



# Plot a Heatmap to Visually Analyse your NaN Values
sns.heatmap(titanic_data.isnull().yticklabels==False)
sns.heatmap(titanic_data.isnull().yticklabels==False, cmap="viridis")



# So here we pick the Age Column VS the Class
sns.boxplot(x="Pclass", y="Age", data=titanic_data)


# So we apply Logistic Regression in cleaning the Data

# Drop the Cabin Column
titanic_data.drop("Cabin", axis=1, inplace=True)
titanic_data.head(5)



# Drop the NaN Values
titanic_data.dropna(inplace=True)
sns.heatmap(titanic_data.isnull().yticklabels==False, cbar=False)



# Check for the Sums
titanic_data.isnull().sum()



# Convert our String Values to Categorical Variables in order to Implement Logistic Regression
pd.get_dummies(titanic_data["Sex"])
sex = pd.get_dummies(titanic_data["Sex"], drop_first=True)
sex.head(5)



# Convert our Embark Values to Categorical Variables
embark = pd.get_dummies(titanic_data["Embarked"], drop_first=True)
embark.head(5)



# Convert our Pclass Values to Categorical Variables
Pcl = pd.get_dummies(titanic_data["Pclass"], drop_first=True)
Pcl.head(5)



# Concat all new Rows into our Dataset
titanic_data = pd.concat([titanic_data, sex, embark, Pcl], axis=1)
Pcl.head(5)



# We will drop the other old Columns
titanic_data.drop(["Sex", "Embarked", "PassengerId", "Name", "Ticket", "Pclass"], axis=1, inplace=True)
titanic_data.head()



# Train Data

# Dependent and Independent Variables
X = titanic_data.drop(["Survived"], axis=1)
y = titanic_data["Survived"]



# Split Data into Training and Testing
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=1)



# So we are going to grab from Linear Regression and fit our dataset
from sklearn.linear_model import LogisticRegression
logmodel = LogisticRegression()
logmodel.fit(X_train, y_train)



# Make Predictions
predictions = logmodel.predict(X_test)



# Model Evaluation

# Classification Report
from sklearn.metrics import classification_report
classification_report(y_test, predictions)



# Confusion Matrix
from sklearn.metrics import confusion_matrix
confusion_matrix(y_test, predictions)



# Calculation of Acuracy Score
from sklearn.metrics import accuracy_score
accuracy_score(y_test, predictions)
