#p3
from os import dup2
import pandas as pd
data = pd.read_csv("data2023.csv")
print(data)
print()

#fill slary with mean value

f1 = data.fillna({"Salary":data["Salary"].mean()})

# fill salary with constant value

f2 = data.fillna({"Salary": 8000})

# fill age with mean value

f3 = data.fillna({"Age":data["Age"].mean()})

# fill age with constant value 

f4 = data.fillna({"Age": 22})

#all together

f6 = data.fillna({
    "Age": 20,
    "Position":"Bench",
    "Experience": data["Experience"].mean(),
    "Salary": data["Salary"].mean()


})

#print

print(f1)

print()

print(f2)

print()

print(f3)

print()

print(f4)

print()

print(f6)

print()

print(data)



#change to data 

data.fillna({
    "Age": 20,
    "Position":"Bench",
    "Experience": data["Experience"].mean(),
    "Salary": data["Salary"].mean()
},inplace=True)


print()
print(data)

data.to_csv("ndata2023.csv")