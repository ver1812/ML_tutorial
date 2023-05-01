# import lib
import pandas as pd 
from sklearn.model_selection import train_test_split 
from sklearn.tree import DecisionTreeClassifier, plot_tree 
from sklearn.metrics import classification_report 
import matplotlib.pyplot as plt

# load the data
data = pd.read_csv("titanic_data_m2023.csv")
print(data)
data.drop(["PassengerId", "Name", "Ticket", "Cabin"], axis="columns", inplace=True)
print(data)
# check for null data
print(data.isnull().sum())

# handle null data
data.fillna({
"Age": data[ "Age" ].mean(),
"Embarked" : "C"
}, inplace=True)

# check for null data
print (data.isnull().sum())
# features and target
features = data.drop ("Survived", axis="columns")
target = data["Survived"]
# handle Cat Data
nfeatures = pd.get_dummies(features)
print(features)
print (nfeatures)
# train and test
x_train, x_test, y_train, y_test = train_test_split(nfeatures, target)
# model
model = DecisionTreeClassifier()
model.fit (x_train, y_train)
# classification report
cr = classification_report (y_test, model.predict (x_test))
print(cr)
# predict
d = [[3, 22.000000, 1, 0, 7.2500, 0, 1, 0, 0, 1]]
ans = model.predict(d)
print(ans)
# internal working
plot_tree(model)
plt.show()