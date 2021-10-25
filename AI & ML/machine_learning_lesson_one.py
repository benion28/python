# Check the versions of libraries

# Python Version
import sys
print(f"Python: { sys.version }")

# Scipy
import scipy
print(f"Scipy: { scipy.__version__ }")

# Numpy
import numpy
print(f"Numpy: { numpy.__version__ }")

# Matplotlib
import matplotlib
print(f"Matplotlib: { matplotlib.__version__ }")

# Pandas
import pandas
print(f"Pandas: { pandas.__version__ }")

# Scikit-Learn
import sklearn
print(f"Sklearn: { sklearn.__version__ }")



# Load Libraries
import pandas
from pandas.plotting import scatter_matrix
import matplotlib.pyplot as plt
from sklearn import model_selection
from sklearn.metrics import classification_report
from sklearn.metrics import confusion_matrix
from sklearn.metrics import accuracy_score
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis
from sklearn.naive_bayes import GaussianNB
from sklearn.svm import SVC



# Load Data
url = "C:\\Benion\\Benion Programmings\\Python\\AI & ML\\data\\iris.data"
names = ["sepal-length", "sepal-width", "petal-length", "petal-width", "class"]
dataset = pandas.read_csv(url, names=names)



# Data Shape
print(dataset.shape)



# Summary Values (Mean, SD, Min, Max, 25%, 50%, 75%, Count)
print(dataset.describe())



# Number of Instances that Belongs to each Class
print(dataset.groupby("class").size())



# Sample Dataset (First 30 Data)
print(dataset.head(30))



# Create An Univariated Plot
dataset.plot(kind="box", subplots=True, layout=(2, 2), sharex=False, sharey=False)
plt.show()



# Create An Histogram
dataset.hist()
plt.show()



# Create A Multi-variated Plot (Scatter Plot)
scatter_matrix(dataset)
plt.show()



# Validation Dataset
array = dataset.values
X = array[:, 0:4]
Y = array[:, 4]
validation_size = 0.20
seed = 6
X_train, X_test, Y_train, Y_test = model_selection.train_test_split(X, Y, test_size=validation_size, random_state=seed)



# A Test Harness (Split our dataset into 10 parts, train on 9 and test on 1)
seed = 6
scoring = "accuracy"



# Spot Check Algorithms
models = []
models.append(("LR", LogisticRegression()))
models.append(("LDA", LinearDiscriminantAnalysis()))
models.append(("KNM", KNeighborsClassifier()))
models.append(("CART", DecisionTreeClassifier()))
models.append(("NB", GaussianNB()))
models.append(("SVM", SVC()))

# Evaluate Each Model in Turn
results = []
names = []
for name, model in models:
    kfold = model_selection.KFold(n_splits=10, random_state=seed)
    cv_results = model_selection.cross_val_score(model, X_train, Y_train, cv=kfold, scoring=scoring)
    results.append(name)
    message = "%s: %f (%f)" % (name, cv_results.mean(), cv_results.std())
    print(message)

