import pandas as pd 
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt
data = pd.read_csv("temp_pressure_march2023.csv")
print (data)
feature = data[["temp"]]
target = data["pressure"]
model = LinearRegression()
model.fit (feature, target)

plt.scatter (data["temp"], data["pressure"], color="red") 
plt.plot (data["temp"], model.predict (feature), color="blue") 
plt.show()