#p3
import pandas as pd
from sklearn.linear_model import LinearRegression

data = pd.read_csv("hpmarch2023.csv")
feature = data[["area"]]
target = data[["price"]]

print(feature)
print(target)

model = LinearRegression()
model.fit(feature,target)

b0 = model.intercept_
b1 = model.coef_
print("b0 =",b0)
print("b1 = ",b1)

area= float(input("Enter area "))
price = b0 + b1 * area
print("price = ",price)