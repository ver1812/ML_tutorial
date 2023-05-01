import pandas as pd
from sklearn.linear_model import LinearRegression

data = pd.read_csv("abpm2023.csv")

features = data[["area","bedrooms"]]
target = data["price"]

model = LinearRegression()
model.fit(features, target)

area = float(input("Enter area "))
br = float(input("Enter bedrooms "))
price = model.predict([[area,br]])

print("price = ",price)
