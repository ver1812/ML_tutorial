# linear regression
import pandas as pd
from sklearn.linear_model import LinearRegression
data = pd.read_csv("pos_salary_march2023.csv")
print (data)
feature = data[["Level"]]
target = data["Salary"]
model = LinearRegression()
model.fit(feature, target)
level = float(input("enter level "))
salary = model.predict([[level]])
print("salary = ", salary)