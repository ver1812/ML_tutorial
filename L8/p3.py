import pandas as pd 
from sklearn.linear_model import LogisticRegression
data = pd.read_csv("vehicle_data_m2023.csv")
print(data)
feature = data[ ["Age"] ]
target = data ["Vehicle"]

model = LogisticRegression()
model. fit(feature, target)
age = float(input("enter age "))
res = model.predict_proba([[age]])
print(res)
r = res.ravel().tolist ()
print (r)
rbike = round(r[0] * 100,2)
rcar = round(r[1] * 100,2)
rcycle = round(r [2] * 100,2)
print("bike ", rbike)
print("car " , rcar)
print("cycle ", rcycle)