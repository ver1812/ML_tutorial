import pandas as pd
from sklearn.linear_model import LinearRegression

data = pd.read_csv("esm2023.csv")

feature = data[["exp"]]
target = data["sal"]

model = LinearRegression()
model.fit(feature, target)

exp = float(input("Enter exp "))
sal = model.predict([[exp]])

print("salary = ",sal)
