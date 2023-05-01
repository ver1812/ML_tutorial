#boston housing dataset
# import lib
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
# load the data
data = pd.read_csv("HousingData.csv")
print(data)
# check for null data
res = data.isnull().sum()
print(res)
# handle null data
data.fillna({
"CRIM" : data ["CRIM"].mean(),
"ZN" : data ["ZN"].mean(),
"INDUS" : data[ "INDUS"]. mean(),
"AGE" : data ["AGE"].mean(),
"CHAS" : data ["CHAS"].mean(),
"LSTAT" : data ["LSTAT"].mean(),
}, inplace=True)

# check for null data again
res = data.isnull().sum()
print(res)
print(data)
# features and target
features = data.drop(["MEDV"], axis="columns")
target = data ["MEDV"]
print(features.head())
print(target.head())
# train and test
x_train, x_test, y_train, y_test = train_test_split(features, target)
# model and score
model = LinearRegression()
model.fit(x_train, y_train)

s1 = model.score(x_train, y_train)
s2 = model.score(x_test, y_test)
print("train perf " ,s1)
print("test perf", s2)
# predict
d = [[0.00632, 18.0,
2.31, 0.0, 0.538, 6.575, 65.2, 4.0900, 1, 296, 15.3, 396.90,
4.98000077]]
price = model.predict(d)
print("price = ", price)