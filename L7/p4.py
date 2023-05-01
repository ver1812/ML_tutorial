#Logistic Regression

import pandas as pd
from sklearn.linear_model import LogisticRegression

data = pd.read_csv("insurance_data_m23.csv")
print(data)
feature = data[["age"]]
target = data["have_insurance"]

model = LogisticRegression()
model.fit(feature, target)

b0 = model.intercept_
b1 = model.coef_

age = float(input("Enter age "))
num = 1
den = (1 + 2.71 ** (-1 * (b0 + b1 * age)))
hi = num/den

print(hi)
if hi > 0.5 :
    print("yes")
else:
    print("no")