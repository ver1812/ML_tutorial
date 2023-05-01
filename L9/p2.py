# import lib
import pandas as pd 
from sklearn.naive_bayes import BernoulliNB

# load the data
data = pd.read_csv("go_sh_data_m2023.csv")
print (data)

# check for null data
print(data.isnull ().sum())

# feature and target
features = data[ ["Weather", "Car"]]
target = data[ "Result"]

# handle cat data
nfeatures = pd.get_dummies(features)
print (features)
print (nfeatures)

# model
model = BernoulliNB()
model.fit(nfeatures, target)

# predict
we = int(input ("1 rainy and 2 for sunny "))
if we == 1:
    d = [1, 0]
else:
    d = [0, 1]

car = int(input ("1 broken and 2 working "))
if car == 1:
    d = d + [1, 0]
else:
    d = d + [0, 1]
print(d)

ans = model.predict ([d])
print(ans)

# internal working
res = model.predict_proba([d])
r = res.ravel().tolist()
pgo = round(r [0], 2)
psh = round(r [1], 2)
print ("go = ", pgo)
print("sh = ", psh)