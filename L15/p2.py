# Customer Segmentation

# import lib
import pandas as pd 
from sklearn.preprocessing import MinMaxScaler 
from sklearn.cluster import KMeans 
import matplotlib.pyplot as plt
# load the data
data = pd.read_csv ("Mall_Customers_m2023.csv")
print (data)
# check for null data
print(data.isnull().sum())
# features
features = data [ ["Annual_Income", "Spending_Score"]]

# feature scaling
mms = MinMaxScaler ( )
nfeatures = mms.fit_transform(features)
print(features)
print (nfeatures)

# model
model = KMeans (n_clusters=5, random_state=1)
res = model.fit_predict(nfeatures)
data ["clusters"] = res
print (data.head(10))

# MI MS
# HI LS
# HI HS
# LI HS
# LI LS

d0 = data [data.clusters==0]  
d1 = data[data.clusters==1]
d2 = data[data.clusters==2]
d3 = data[data.clusters==3]
d4 = data[data.clusters==4]

plt.scatter (d0["Annual_Income"], d0["Spending_Score"], color="red", label="MI MS") 
plt.scatter (d1["Annual_Income"], d1["Spending_Score"], color="green", label="HI LS") 
plt.scatter (d2["Annual_Income"], d2["Spending_Score"], color="blue", label="HI HS") 
plt.scatter (d3["Annual_Income"], d3["Spending_Score"], color="pink", label="LI HS") 
plt.scatter (d4["Annual_Income"], d4["Spending_Score"], color="brown", label="LI Ls") 
plt.legend()
plt.show()
# predict

ai = float (input ("enter annual income "))
ss = float (input ("enter spending score "))
d = [[ai, ss]]
nd = mms.transform(d)
ans = model.predict (nd)

if ans == 0:
    print ("MI MS")
elif ans == 1:
    print( "HI LS")
elif ans == 2:
    print ( "HI HS")
elif ans == 3:
    print ("LI HS")
else:
    print("LI LS")