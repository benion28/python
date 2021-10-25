import pandas as pd
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
import joblib
from sklearn import tree

music_data = pd.read_csv("C:\\Benion\\Benion Programmings\\Python\\AI & ML\\data\\music.csv")
music_data



X = music_data.drop(columns=["Genre"])
X



y = music_data["Genre"]
y



model = DecisionTreeClassifier()
model.fit(X, y)



predictions = model.predict([ [21, 1], [22, 0] ])
predictions



X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

model_dt = DecisionTreeClassifier()
model_dt.fit(X_train, y_train)
prediction = model_dt.predict(X_test)

score = accuracy_score(y_test, prediction)
score



model_export = DecisionTreeClassifier()
model_export.fit(X, y)

joblib.dump(model_export, "C:\\Benion\\Benion Programmings\\Python\\AI & ML\\data\\music-recommender.joblib")



model_import = joblib.load("C:\\Benion\\Benion Programmings\\Python\\AI & ML\\data\\music-recommender.joblib")

predict = model.predict([ [21, 1] ])
predict



tree.export_graphviz(model_import, out_file="C:\\Benion\\Benion Programmings\\Python\\AI & ML\\data\\music-recommender.dot",
                     feature_names=[ "age", "gender" ],
                     class_names=sorted(y.unique()),
                     label="all",
                     rounded=True,
                     filled=True)
