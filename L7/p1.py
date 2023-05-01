import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report,ConfusionMatrixDisplay

#load the data

data = pd.read_csv("result_data_sep2022.csv")
print (data)
# check for null data
res = data.isnull ().sum()
print(res)
# features and target
feature = data[[ "hr"]]
target = data ["result"]
# train and test
x_train, x_test, y_train, y_test = train_test_split(feature, target, test_size=0.4)
# model
model = LogisticRegression()
model.fit (x_train, y_train)
disp = ConfusionMatrixDisplay.from_estimator (model, x_test, y_test) 
print(disp.confusion_matrix)
cr = classification_report(y_test, model.predict (x_test))
print(cr)