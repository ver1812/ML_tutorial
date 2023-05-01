# import lib I
import pandas as pd
from sklearn.preprocessing import MinMaxScaler
from sklearn.neighbors import KNeighborsClassifier

# load the data
data = pd.read_csv("tshirt_data_m23.csv")
print(data)

# check for null data
print (data.isnull().sum())

# feature and target
features = data[ ["Height(cm)", "Weight(kg)"]]
target = data["T-Shirt Size"]
print(features)
print(target)

# feature scaling
mms = MinMaxScaler()
features = mms.fit_transform(features)
print(features)

# model
model = KNeighborsClassifier (n_neighbors=3, metric="euclidean")
model.fit(features, target)

# predict
height = float(input("enter height "))
weight = float(input("enter weight "))
data = [[height, weight]]
ndata = mms.transform(data)

size = model.predict(ndata)
print(size)
# internal working
nn = model.kneighbors(ndata,n_neighbors=3)
print(nn)