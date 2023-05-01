#import library

import pandas as pd
from sklearn.linear_model import LinearRegression

# s2: load data
data = pd.read_csv("abpm2023.csv")
print(data)

# s3: features and target
features = data[["area","bedrooms"]]
target = data["price"]


model = LinearRegression()
model.fit(features,target)

b0 = model.intercept_
b1 = model.coef_[0]
b2 = model.coef_[1]

print("b0 = ",b0)
print("b1 = ",b1)
print("b2 = ",b2)

