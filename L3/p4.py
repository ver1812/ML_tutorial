#import library

import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split

# load data 
data = pd.read_csv("exp_test_sal2023.csv")
print(data)

#features and target

features = data[["exp","test"]]
target = data["salary"]

print(features)
print(target)

model = LinearRegression()
model.fit(features,target)

b0 = model.intercept_
b1 = model.coef_[0]
b2 = model.coef_[1]

print("b0 = ",b0)
print("b1 = ",b1)
print("b2 = ",b2)
