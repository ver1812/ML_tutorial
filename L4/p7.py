# import lib
import pandas as pd
from sklearn.linear_model import LinearRegression
# load the data
data = pd.read_csv("fruit_qty_price_march2023.csv")

# check for null data
print(data)
print()
res = data.isnull().sum()
print(res)
print()

# handle the null data
data.fillna({
"name": "Mango",
"price" : data["price"].mean()
}, inplace=True)
# check if null data is handled
print(data)
print()
res = data.isnull().sum()
print(res)
print()

# handle cat data
dummies = pd.get_dummies(data.name)
print(dummies)
print()
ndata = pd.concat([data, dummies], axis=1)
print(ndata)
print()

# features and target
features = ndata[["quantity","Apple", "Mango"]]
target = ndata["price"]

# model
model = LinearRegression()
model.fit(features, target)
# take input from user
qty = float(input ("enter qty "))
name = int(input("1 Apple and 2 Mango "))
if name == 1:
    d = [[qty, 1, 0]]
elif name == 2:
    d = [[qty, 0, 1]]
# predict

price = model.predict(d)
print("price = ", price)