import pandas as pd 
import numpy as np 
from sklearn.impute import SimpleImputer
from sklearn.linear_model import LinearRegression
data = pd.read_csv("apple2023.csv")
print (data)
print()
res = data.isnull().sum()
print(res)
print()

s1 = SimpleImputer(missing_values=np.nan, strategy="median")
data["price"] = s1.fit_transform(data[["price"]])
print(data)
print()

res = data.isnull().sum()
print(res)
print()

feature = data[["qty"]]
target = data["price"]
model = LinearRegression()
model.fit(feature,target)
qty = float(input ("enter qty "))
price = model.predict([[qty]])
print("price = ",price)
