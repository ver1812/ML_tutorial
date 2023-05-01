import pandas as pd
from sklearn.linear_model import LinearRegression

data = pd.read_csv("temp_pressure_march2023.csv")
print(data)

feature = data[["temp"]]
target = data["pressure"]

model = LinearRegression()
model.fit(feature,target)

temp = float (input ("enter temp "))
pressure = model.predict ( [ [temp]])
print ("pressure" , pressure)

# Wrong type as this is not linear regression but polynomial regression