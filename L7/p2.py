# data analysis

import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv("insurance_data_m23.csv")
print(data)

x = data["age"]
y = data["have_insurance"]

plt.scatter(x,y,color='brown')
plt.xlabel("Age")
plt.ylabel("Have Insurance")
plt.show()