# data analysis
import pandas as pd 
import matplotlib.pyplot as plt
data = pd.read_csv("temp_pressure_march2023.csv")
print (data)
x = data ["temp"]
y = data["pressure"]
plt.scatter (x, y, color="red")
plt.xlabel("Temp") 
plt.ylabel("Pressure")
plt.show()