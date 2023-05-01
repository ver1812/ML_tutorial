# data analysis

import pandas as pd 
import matplotlib.pyplot as plt
data = pd.read_csv("result_data_sep2022.csv")
print(data)
x = data ["hr"]
y = data["result"]
plt.scatter (x, y, color="red")
plt.xlabel( "Hours")
plt.ylabel("Result") 
plt.show()