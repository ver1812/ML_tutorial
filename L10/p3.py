# import lib
import pandas as pd 
import numpy as np 
from sklearn.preprocessing import MinMaxScaler 
from sklearn.model_selection import train_test_split 
from sklearn.neighbors import KNeighborsClassifier 
from sklearn.metrics import classification_report

# load the data
data = pd.read_csv("diabetes m23.csv")
print(data)

# check data
data[["Glucose","BloodPressure","SkinThickness", "Insulin", "BMI"]]=data[["Glucose",
"BloodPressure","SkinThickness", "Insulin", "BMI"]].replace(0, np.NAN)

# understand data
print(data.isnull().sum())

# handle null data

data.fillna({
    "Glucose": data["Glucose"].mean (),
    "BloodPressure": data["BloodPressure"].mean(),
    "SkinThickness": data["SkinThickness"].mean(),
    "Insulin": data["Insulin"].mean(),
    "BMI": data["BMI"].mean(),
}, inplace=True)

# understand data
print(data.isnull().sum())

# features and target
features = data.drop ("Outcome", axis="columns")
target = data[ "Outcome"]
print(features)
print(target)

# feature scaling
mms = MinMaxScaler()
nfeatures = mms.fit_transform(features)
print(nfeatures)

# find value of N
# find value of N
N = int(len (data) ** 0.5)
if N % 2 == 0:
    N = N + 1

# train and test
x_train, x_test, y_train, y_test = train_test_split(nfeatures, target)
# model
model = KNeighborsClassifier(n_neighbors=N, metric="euclidean")
model.fit(x_train, y_train)

# classification report
cr = classification_report(y_test, model.predict(x_test))
print(cr)
