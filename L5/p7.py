# why it is going wrong

import pandas as pd 
import matplotlib.pyplot as plt 
from sklearn.linear_model import LinearRegression
data = pd.read_csv("pos_salary_march2023.csv")
print(data)
feature = data[["Level"]]
target = data["Salary"]
model = LinearRegression()
model.fit(feature, target)
plt.scatter(data["Level"], data["Salary"], color="red") 
plt.plot (data["Level"], model.predict(feature), color="green") 
plt.show()