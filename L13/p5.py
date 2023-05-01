# import lib
import pandas as pd 
from sklearn.cluster import KMeans 
import matplotlib.pyplot as plt
# load the data
data = pd.read_csv("xy_data_m2023.csv")
print (data)
# check for null data
print(data.isnull().sum())
# features
features = data[["X", "Y"]]
# model
model = KMeans(n_clusters=2)
res = model.fit_predict(features)
data["cluster"] = res
print (data)
# predict
x = float (input ("enter value of x "))
y = float (input ("enter value of y "))
d = [[x, y]]
ans = model.predict (d)
print (ans)
# internal working
print (model.cluster_centers_)
plt.scatter (data["X"], data["Y"], c=data["cluster"])
plt.show()