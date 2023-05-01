# import lib
import pandas as pd
from sklearn.tree import DecisionTreeClassifier, plot_tree 
import matplotlib.pyplot as plt

# load the data
data = pd.read_csv("loan_default_m2023.csv")
print(data)

# understand the data
print(data.isnull().sum())
# feature and target
features = data [["GENDER", "OCCUPATION" ]]
target = data ["DEFAULT"]

# handle cat data
nfeatures = pd.get_dummies (features)
print (features)
print(nfeatures)

# model
model = DecisionTreeClassifier()
mf = model.fit (nfeatures, target)

# predict
ge = int (input ("1 female and 2 male "))
if ge == 1:
    d = [1, 0]
else:
    d = [0, 1]
oc = int(input ("1 business and 2 salary "))
if oc == 1:
    d = d + [1, 0]
else:
    d = d + [0, 1]

ans = model.predict([d])
print(ans)

# internal working
plot_tree(mf, feature_names=[ "GENDER", "GENDER", "OCCUPATION" , "OCCUPATION"],
           class_names=["loan de de" , "loan mat de"], filled=True) 
plt.show()