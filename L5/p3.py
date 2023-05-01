# import lib
import pandas as pd 
from sklearn.linear_model import LinearRegression 
from sklearn.preprocessing import OneHotEncoder 
from sklearn.compose import ColumnTransformer
# load the data
data = pd.read_csv("place_area_price_march2023.csv")
print(data)
# features and target
features = data[["place", "area"]]
target = data["price"]
# handle cat data
ct = ColumnTransformer([("place", OneHotEncoder(), [0])], remainder="passthrough")
tfeatures = ct.fit_transform(features)
print(features)
print (tfeatures)
nfeatures = pd.DataFrame(tfeatures[:, :], columns=["Karjat", "Khandala", "Lonavala", "area"])
print (nfeatures)
# model

model = LinearRegression()
model.fit(nfeatures, target)
# predict
place = int(input("1 karjat, 2 khandala, 3 lonavala "))
area = float(input("enter area "))
if place == 1:
    d = [[1, 0, 0, area]]
elif place == 2:
    d = [[O, 1, 0, area]]
else:
    d = [[0, 0, 1, area]]

price = model.predict(d)
print("price = " ,price)