# data analysis

import pandas as pd 
import matplotlib.pyplot as plt
data = pd.read_csv("pos_salary_march2023.csv")
print (data)
x = data["Level"]
y = data ["Salary"]
plt.scatter(x, y, color="red")
plt.xlabel("Level") 
plt.ylabel ("Salary") 
plt.title("TCS")
plt.show()