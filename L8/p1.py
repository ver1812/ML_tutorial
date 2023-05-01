import pandas as pd 
import matplotlib.pyplot as plt
data = pd.read_csv("vehicle_data_m2023.csv")
print (data)
x = data[ "Age" ]
y = data ["Vehicle"]
plt.scatter(x, y, color="brown")
plt.xlabel ("Age") 
plt.ylabel("Vehicle") 
plt.show()