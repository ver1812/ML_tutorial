

#import library

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

# load data 
# s2: load data
data = pd.read_csv("esm2023.csv")
print(data)

# s3: features and target
feature = data[["exp"]]
target = data["sal"]

print(feature)
print(target)

# s4: train data ==> model and test data ==› score
x_train, x_test , y_train, y_test = train_test_split(feature, target,random_state=120,test_size=0.3)
print(x_train)

print(x_test)


model = LinearRegression()
model.fit(x_train,y_train)

#score 

s1 = model.score(x_train,y_train)
s2 = model.score(x_test,y_test)
print("Train perform = ",round(s1 * 100,2))
print("Test perform = ",round(s2 * 100,2))

#predict
exp = float(input("Enter exp "))
sal = model.predict([[exp]])
print("price = ",sal)
