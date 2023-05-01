#WAPP  to find null data

import pandas as pd
data = pd.read_csv("data2023.csv")
print(data)

#column wise count of null data

r1 = data.isnull().sum()
print(r1)

#salary is null
r2 = data[data.Salary.isnull()]
print(r2)

#exp is null
r3 = data[data.Experience.isnull()]
print(r3)

#age is null
r4 = data[data.Age.isnull()]
print(r4)

#age and position is null
r5 = data[(data.Age.isnull()) & (data.Position.isnull())]
print(r5)


#any column is null
r6 = data[data.isnull().any(axis=1)]
print(r6)

