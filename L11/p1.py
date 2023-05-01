# import lib
import pandas as pd 
from sklearn.preprocessing import MinMaxScaler 
from sklearn.neighbors import KNeighborsRegressor
# load the data
data = pd.read_csv("weight_data_m23.csv")
print (data)
# check for null data
print(data.isnull().sum())
# features and target
features = data[ ["HEIGHT", "AGE"]]
target = data["WEIGHT"]

# feature scaling
mms = MinMaxScaler ()
nfeatures = mms.fit_transform(features)
print(features)
print(nfeatures)
# find value of N

N = int(len (data) ** 0.5)
if N % 2 == 0:
    N = N + 1

# model

model = KNeighborsRegressor(n_neighbors=N, metric="euclidean")
model.fit(nfeatures,target)

# predict
ht = float (input ("enter height "))
ag = float (input ("enter age "))
d = [[ht, ag]]
nd = mms.transform(d)
ans = model.predict (nd)
print(ans)
# internal working

nn = model.kneighbors (nd, _neighbors=N)
print (nn)
