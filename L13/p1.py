# import lib
import pandas as pd 
from sklearn.tree import DecisionTreeClassifier 
import matplotlib.pyplot as plt
# load the data
data = pd.read_csv("car_data_m2023.csv")
data.columns = ["buying","maintenance" , "doors", "persons", "luggage_space", "safety","condition"]
print(data)

# check for null data
print(data.isnull ().sum())
# feature and target
features = data.drop("condition", axis="columns")
target = data["condition"]

# handle cat data
nfeatures = pd.get_dummies(features)
print(features)
print (nfeatures)
nfeatures.to_csv("nf.csv")
# model
model = DecisionTreeClassifier()
model.fit (nfeatures, target)
# feature importance
print(model.feature_importances_)
x = nfeatures.columns
y = model.feature_importances_
plt.figure(figsize= (15,7))
plt.barh(x, y) 
plt.show()