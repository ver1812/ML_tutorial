# import lib 
import pandas as pd
from sklearn.preprocessing import MinMaxScaler
from sklearn.neighbors import KNeighborsClassifier

# load the data
data = pd.read_csv("health_data_m23.csv")
print(data)

# check for null data
print (data.isnull().sum())

# feature and target
features = data[ ["Weight", "Height"]]
target = data["Class"]
print(features)
print(target)

# feature scaling
mms = MinMaxScaler()
nfeatures = mms.fit_transform(features)
print(features)

N = int(len(data) ** 0.5)
if N%2 ==0:
    N = N + 1

# model
model = KNeighborsClassifier (n_neighbors=N, metric="euclidean")
model.fit(nfeatures, target)

# predict
height = float(input("enter height "))
weight = float(input("enter weight "))
data = [[ weight,height]]
ndata = mms.transform(data)

size = model.predict(ndata)
print(size)
# internal working
nn = model.kneighbors(ndata,n_neighbors=N)
print(nn)