# import lib
import pandas as pd 
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report
# load the data
data = pd.read_csv ("car_data_m2023.csv")
data.columns = ["buying", "maintenance", "doors", "persons", "luggage_space", "safety","condition"]
data.drop(["buying", "maintenance", "doors", "luggage_space"], axis="columns", inplace=True)
print(data)
# check for null data
print(data.isnull().sum())
# feature and target
features = data.drop ("condition", axis="columns")
target = data["condition"]

# handle cat data
nfeatures = pd.get_dummies(features)
print(features)
print (nfeatures)
nfeatures.to_csv("nf1.csv")
# train test split
x_train, x_test, y_train, y_test = train_test_split(nfeatures, target)
# model
model = RandomForestClassifier()
model.fit (x_train, y_train)

# classification report
cr = classification_report(y_test, model.predict (x_test))
print(cr)
# predict
d = [[1, 0, 0, 0, 0, 1]]
d = [[ 0, 0, 1, 1, 0, 0]]
d = [[0, 0, 1, 0, 0, 1]]
ans = model.predict (d)
print ("ans = ", ans)