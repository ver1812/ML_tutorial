#Logistic Regression

import pandas as pd
from sklearn.linear_model import LogisticRegression

data = pd.read_csv("insurance_data_m23.csv")
print(data)
feature = data[["age"]]
target = data["have_insurance"]

model = LogisticRegression()
model.fit(feature, target)
age = float (input("enter age "))
hi = model.predict([[age]])
print("hi ", hi)

