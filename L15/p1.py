# find number of clusters
# import lib
import pandas as pd
from sklearn.cluster import KMeans 
import matplotlib.pyplot as plt 
import warnings 
warnings.filterwarnings("ignore")
# load the data
data = pd.read_csv("Mall_Customers_m2023.csv")
print (data)
# check null data
print(data.isnull().sum())
# features
features = data [ ["Annual_Income", "Spending_Score"]]
# compute inertia

num, val = [], []
for i in range(1, 10):
    model = KMeans(n_clusters=i)
    model.fit(features)
    num. append(i)
    val. append (model.inertia_)
# plot
plt.plot(num, val)
plt.xlabel("Number of clusters") 
plt.ylabel("Inertia") 
plt.show()