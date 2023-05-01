import pandas as pd 
from sklearn.linear_model import LinearRegression 
from sklearn.preprocessing import PolynomialFeatures
import matplotlib.pyplot as plt
data = pd.read_csv("temp_pressure_march2023.csv")
print(data)
feature = data[ ["temp"]]
target = data["pressure"]
pf = PolynomialFeatures (degree=3)
pfeature = pf.fit_transform(feature)
print(feature)
print (pfeature)
model = LinearRegression ()
model.fit (pfeature, target)
plt.scatter(data["temp"], data["pressure"], color="red") 
plt.plot(data["temp"], model.predict (pfeature), color="blue") 
plt.show()
