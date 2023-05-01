import pandas as pd 
from sklearn.linear_model import LinearRegression
data = pd.read_csv("place_area_price_march2023.csv")
print (data)
print()


dummies = pd.get_dummies(data.place)
print(dummies)
print()

ndata = pd.concat([data, dummies], axis="columns")
print(ndata)
print()

features = ndata[["area", "Karjat" , "Khandala" , "Lonavala"]]
target = ndata["price"]
print(features)
print()

print(target)
print()

model = LinearRegression()
model.fit(features, target)

area = float (input("enter area "))
place = int(input("1 Karjat, 2 Khandala and 3 Lonavala "))
if place == 1:
    d = [[area, 1, 0, 0]]
elif place == 2:
    d = [[area, 0, 1, 0]]
elif place == 3:
    d = [[area, 0, 0, 1]]
price = model.predict(d)
print("price = ", price)
