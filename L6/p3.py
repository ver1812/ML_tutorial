import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures
data = pd.read_csv("temp_pressure_march2023.csv")
print (data)
feature = data [["temp"]]
target = data["pressure"]
pf = PolynomialFeatures (degree=3)
pfeature = pf.fit_transform(feature)
print (feature)
print (pfeature)
model = LinearRegression()
model.fit (pfeature, target)
temp = float (input ("enter temp "))
ptemp = pf.fit_transform([[temp]])
pressure = model.predict(ptemp)
print ("pressure ", pressure)