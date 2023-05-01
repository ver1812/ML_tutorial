

#import library

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

# s2: load data
data = pd.read_csv("abpm2023.csv")
print(data)

# s3: features and target
features = data[["area","bedrooms"]]
target = data["price"]
print(features)
print(target)

# s4: train data ==> model and test data ==› score
x_train, x_test , y_train, y_test = train_test_split(features, target,random_state=120)


model = LinearRegression()
model.fit(x_train,y_train)

s1 = model.score(x_train,y_train)
s2 = model.score(x_test,y_test)
print("Train perf ",s1)
print("Test perf ",s2)

# predict
area = float(input("Enter area "))
br = float(input("Enter bedrooms "))
price = model.predict([[area,br]])
 
print("price = ",price)

#internal formula 

b0 = model.intercept_
b1 = model.coef_[0]
b2 = model.coef_[1]
aprice = b0 + b1 * area + b2 * br
print("aprice = ",aprice)


