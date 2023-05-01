#P3

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

# s4: train data ==> model and test data ==› score
x_train, x_test , y_train, y_test = train_test_split(features, target,random_state=112)

model = LinearRegression()
model.fit(x_train,y_train)

s1 = model.score(x_train,y_train)
s2 = model.score(x_test,y_test)
print("Train perf ",s1)
print("Test perf ",s2)

#predict
exp = float(input("Enter exp "))
test = float(input("Enter test "))

salary = model.predict([[exp,test]])
print("Salary = ",salary)

#internal 
b0 = model.intercept_
b1 = model.coef_[0]
b2 = model.coef_[1]

print("b0 = ",b0)
print("b1 = ",b1)
print("b2 = ",b2)

aprice = b0 + b1 * exp + b2 * test
print("aprice = ",aprice)








