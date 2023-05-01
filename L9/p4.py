# import lib
import pandas as pd 
from sklearn.naive_bayes import GaussianNB 
from sklearn.model_selection import train_test_split 
from sklearn.metrics import classification_report

# load the data
data = pd.read_csv( "Social_Network_Ads_m2023.csv")
print(data.shape)
print(data)

# check for null data
print(data.isnull().sum())

# features and target
features = data [["Gender","Age", "EstimatedSalary"]]
target = data["Purchased"]

# handle cat data
nfeatures = pd.get_dummies(features)
print(features)
print(nfeatures)

# train and test
x_train, x_test, y_train, y_test = train_test_split(nfeatures, target)

# model
model = GaussianNB()
model.fit(x_train, y_train)

# performance
cr = classification_report(y_test, model.predict(x_test))
print(cr)

# predict
age = float (input("enter age "))
es = float(input ("enter salary "))

mf = int(input(" 0 for female and 1 for male "))
if mf == 0:
    da = [[age, es, 1, 0]]
else:
    da = [[age, es, 0, 1]]
ans = model.predict (da)
print(ans)