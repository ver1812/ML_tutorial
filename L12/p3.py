# import lib
import pandas as pd 
from sklearn.tree import DecisionTreeClassifier

# load the data
data = pd.read_csv("result_data_m2023.csv")
print(data)

# understand the data
print(data.isnull().sum())
# features and target
feature = data[["hr"]]
target = data[ "result"]

# model
model = DecisionTreeClassifier()
mf = model.fit(feature, target)

#predict
hr = float(input("enter hours "))
res = model.predict([[hr]])
print(res)

# internal working
from sklearn.tree import plot_tree
import matplotlib.pyplot as plt
plot_tree (mf, filled=True, fontsize=20, feature_names=["hr"],class_names= ["Fail", "Pass"])
plt.show()



