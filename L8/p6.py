# import lib
import pandas as pd 
from sklearn.naive_bayes import BernoulliNB

# load data
data = pd.read_csv("play_data_m2023.csv")
print(data)

# handle null data
print(data.isnull().sum())

# feature and target
feature = data [["Weather"]]
target = data["Play"]

# handle cat data
nfeature = pd.get_dummies(feature)
print(feature)
print(nfeature)

# model
model = BernoulliNB()
model.fit(nfeature, target)

# predict
weather = int (input(" 1 for overcast, 2 rainy and 3 sunny "))
if weather == 1:
    d = [[1, 0, 0]]
elif weather == 2:
    d = [[0, 1, 0]]
else:
    d = [[0, 0, 1]]
play = model.predict(d)
print(play)
print(model.predict_proba(d))   