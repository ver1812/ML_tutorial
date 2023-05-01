# polynomial regression
import pandas as pd 
from sklearn.linear_model import LinearRegression 
from sklearn.preprocessing import PolynomialFeatures
data = pd.read_csv("pos_salary_march2023.csv")
print(data)
feature = data[["Level"]]
target = data["Salary"]
pf = PolynomialFeatures(degree=5)
pfeature = pf.fit_transform(feature)
model = LinearRegression()
model.fit (pfeature, target)
level = float(input("enter level "))
plevel = pf.fit_transform([[level]])
salary = model.predict (plevel)
print("salary = ", salary)