# import lib
import pandas as pd 
import numpy as np 
from sklearn.impute import SimpleImputer 
from sklearn.compose import ColumnTransformer 
from sklearn.preprocessing import OneHotEncoder 
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
# load the data
data = pd.read_csv("fruit_qty_price_march2023.csv")
print (data)
# check for null data
res = data.isnull().sum()
print(res)
# handle null data
s1 = SimpleImputer(missing_values=np.nan, strategy="constant",
fill_value="Mango")
data["name"] = s1.fit_transform(data[["name"]])
print (data)
s2 = SimpleImputer(missing_values=np.nan, strategy="mean")
data["price"] = s2.fit_transform(data[["price"]])
print (data)

# check for null data
res = data.isnull().sum()
print(res)

# features and target
features = data[["name", "quantity"]]
target = data["price"]
# handle cat data
ct = ColumnTransformer([ ("name", OneHotEncoder (), [0])], remainder="passthrough")
tfeatures = ct.fit_transform(features)
print (features)
print (tfeatures)
nfeatures = pd.DataFrame(tfeatures [:, :], columns=["Apple", "Mango", "quantity"])
print (nfeatures)

# train and test
x_train, x_test, y_train, y_test = train_test_split (nfeatures, target)
model = LinearRegression ()
model.fit (x_train, y_train)

# score
s1 = model.score (x_train, y_train)
s2 = model.score(x_test, y_test) 
print("train performance", s1)
print("test performance ", s2)

# predict
name = int (input ("1 Apple and 2 Mango "))
qty = float(input("enter qty "))
if name == 1:
    d = [[1, 0, qty]]
else:
    d = [[0, 1, qty]]
price = model.predict (d)
print("price = ", price)