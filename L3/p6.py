#p6
import pandas as pd
from sklearn.linear_model import LinearRegression

data = pd.read_csv("apple2023.csv")
print(data)

res = data.isnull().sum()
print(res)
ndata = data.fillna({"price":data["price"].mean()})
print(ndata)

res = ndata.isnull().sum()
print(res)

#model
feature = ndata[["qty"]]
target = ndata["price"]
model = LinearRegression()
model.fit(feature,target)

#predict

qty = float(input("Enter qty "))
price = model.predict([[qty]])
print("price = ",price)



