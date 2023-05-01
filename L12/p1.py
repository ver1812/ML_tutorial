# import lib
import pandas as pd 
from sklearn.tree import DecisionTreeClassifier

# load the data
data = pd.read_csv("run_data_m2023.csv")
print (data)

# understand the data
print (data.isnull().sum())
# features and target
features = data[["Weather","Just Ate" ]]
target = data[ "Will I Go Running?"]
# handle cat data
nfeatures = pd.get_dummies(features)
print (features)
print (nfeatures)

# model
model = DecisionTreeClassifier()
mf = model. fit(nfeatures, target)

# predict
we = int(input("Weather: 1 rainy and 2 sunny "))
if we == 1:
    d = [1, 0]
else:
    d = [0, 1]
ia = int(input ("Just Ate: 1 yes and no "))
if ia == 1:
    d = d + [0, 1]
else:
    d = d + [1, 0]
ans = model.predict ([d])
print (ans)
# internal working

from sklearn.tree import plot_tree 
import matplotlib.pyplot as plt 
plot_tree(mf, filled=True, feature_names= ["Weather",
"Weather", "Just Ate", "Just Ate"],
class_names = ["Nahin Jaunga", "Bhaag Milkha Bhaag"])
plt.show()