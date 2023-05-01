# import lib
import pandas as pd
from sklearn. tree import DecisionTreeRegressor, plot_tree
import matplotlib.pyplot as plt
# load the data
data = pd.read_csv("salary_data_m2023.csv")
print (data)
# check null data
print(data.isnull().sum())
# feature and target
feature = data[ ["Level"]]
target = data["Salary"]
# model
model = DecisionTreeRegressor ()
mf = model.fit (feature, target)
# predict
level = float (input("enter level "))
salary = model.predict([ [level]])
print("salary = ", salary)
# internal working
plt.figure(figsize=(10, 5))
plot_tree(mf, filled=True, feature_names= ["Level"])
plt.show()