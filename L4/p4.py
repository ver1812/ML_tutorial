import pandas as pd 
from sklearn.linear_model import LinearRegression
data = pd.read_csv("place_area_price_march2023.csv")
print(data)
features = data[["place", "area"]]
target = data["price"]
print(features)
print(target)

model = LinearRegression ()
model.fit (features, target)
# ML app is crashing
# coz ML cannot work with string data --› categorical data
# hence we need to convert cat data into numerical data