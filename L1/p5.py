#p5
# s1: import lib
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression


# s2: load data
data = pd.read_csv("hpmarch2023.csv")
print(data)

# s3: features and target
feature = data[["area"]]
target = data[["price"]]

print(feature)
print(target)

# s4: train data ==> model and test data ==› score
x_train, x_test , y_train, y_test = train_test_split(feature, target)
print(x_train)
print(y_train)
print(x_test)
print(y_test)


model = LinearRegression()
model.fit(x_train,y_train)

score = model.score(x_test,y_test)
print(score)


# s5: predict
area= float(input("Enter area "))
price = model.predict([[area]])
print("price = ",price)