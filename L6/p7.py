# internal working of Logistic Regression
import pandas as pd 
from sklearn.linear_model import LogisticRegression
data = pd.read_csv("result_data_sep2022.csv")
print (data)
feature = data[["hr"]]
target = data["result"]
model = LogisticRegression()
model. fit (feature, target)
b0 = model.intercept_
b1 = model.coef_
hr = float (input ("enter hours "))
num = 1
den = 1 + (2.71) ** (-1 * (b0 + b1 * hr) )
result = num / den
print(result)
if result > 0.5:
    print("Pass")
else:
    print("Fail")