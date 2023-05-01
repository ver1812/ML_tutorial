
import pandas as pd
from sklearn.linear_model import LinearRegression

data = pd.read_csv("hpmarch2023.csv")
feature = data[["area"]]
target = data[["price"]]

print(feature)
print(target)

model = LinearRegression()
model.fit(feature,target)

area= float(input("Enter area "))
price = model.predict([[area]])
print("price = ",price)