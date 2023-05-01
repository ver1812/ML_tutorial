from os import dup2
import pandas as pd
data = pd.read_csv("data2023.csv")
print(data)

# drop the row if any value is null
d1 = data.dropna(how="any")
print(d1)
print()

#drop the row if all value is null
d2 = data.dropna(how="all")
print(d2)
print()


#drop the row if salary is null
d3 = data.dropna(subset=['Salary'])
print(d3)
print()

#drop the row if both age and position is null
d4 = data.dropna(subset=["Age", "Position"], how="all")
print(d4)
