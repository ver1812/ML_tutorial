# Data Analysis

import pandas as pd 
import matplotlib.pyplot as plt

data = pd.read_csv("esm2023.csv")
print(data.head())
print(data.tail())

x = data["exp"]
y = data["sal"]
plt.scatter(x,y)
plt.xlabel("Experience")
plt.ylabel("Salary")
plt.title("TCS")
plt.show()