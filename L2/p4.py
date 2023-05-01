import pandas as pd
from sklearn.linear_model import LinearRegression

data = pd.read_csv("esm2023.csv")

feature = data[["exp"]]
target = data["sal"]

model = LinearRegression()
model.fit(feature, target)

b0 = model.intercept_
b1 = model.coef_

exp = float(input("Enter exp "))
sal = b0 + b1 * exp

print("salary = ",sal)
