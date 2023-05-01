import pandas as pd 
from sklearn.linear_model import LogisticRegression
data = pd.read_csv("vehicle_data_m2023.csv")
print(data)
feature = data [["Age"]]
target = data["Vehicle"]
model = LogisticRegression()
model.fit(feature, target)

age = float(input("enter age "))
vehicle = model.predict([ [age]])
print("vehicle = ", vehicle)