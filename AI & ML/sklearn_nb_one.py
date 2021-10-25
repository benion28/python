# import libraries
from sklearn import datasets
from sklearn import metrics
from sklearn.naive_bayes import GaussianNB



# load datasets
dataset = datasets.load_iris()
print(dataset)



# inspect data
data = dataset.data
print(data)



# inspect target data
target = dataset.target
print(target)



# fit data into model
model = GaussianNB()
model.fit(data, target)



# make predictions
expected = target
predicted = model.predict(data)



# Classification Report
classification_report = metrics.classification_report(expected, predicted)
print(f"Classification Report: {classification_report}")



# Confusion Matrix
confusion_matrix = metrics.confusion_matrix(expected, predicted)
print(f"Confusion Matrix: {confusion_matrix}")







