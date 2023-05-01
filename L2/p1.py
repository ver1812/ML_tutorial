#p1

#import library

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

# load data 
# s2: load data
data = pd.read_csv("hpmarch2023.csv")
print(data)

# s3: features and target
feature = data[["area"]]
target = data["price"]

print(feature)
print(target)

# s4: train data ==> model and test data ==› score
x_train, x_test , y_train, y_test = train_test_split(feature, target,random_state=120)
print(x_train)
print(y_train)
print(x_test)
print(y_test)

model = LinearRegression()
model.fit(x_train,y_train)

#score 

s1 = model.score(x_train,y_train)
s2 = model.score(x_test,y_test)
print("Train perform = ",round(s1 * 100,2))
print("Test perform = ",round(s2 * 100,2))

#predict
area= float(input("Enter area "))
price = model.predict([[area]])
print("price = ",price)
