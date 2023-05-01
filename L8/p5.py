# import lib
# import lib
import pandas as pd 
from sklearn.model_selection import train_test_split 
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import ConfusionMatrixDisplay, classification_report
# load the data
data = pd.read_csv("age_movie_m2023.csv")
print (data)
# check for null data
print(data.isnull().sum())
# features and target
feature = data [["age"]]
target = data["movie"]
# train and test
x_train,x_test,y_train,y_test = train_test_split(feature,target)
# model
model = LogisticRegression()
model.fit (x_train, y_train)
print(x_test)
print(y_test)
print(model.predict(x_test))
# classification matrix
disp = ConfusionMatrixDisplay.from_estimator(model, x_test, y_test) 
print (disp.confusion_matrix)
# classification report
cr = classification_report(y_test, model.predict(x_test))
print (cr)
# predict
age = float(input("Enter age "))
movie = model.predict([[age]])
print(movie)
# internal working
res = model.predict_proba([[age]])
print(res)

r = res.ravel().tolist()
print (r)
print("ddlj ", round(r[0] * 100, 2))
print("harry potter ", round(r[1]*100, 2))
print("monevheist " , round (r[2]*100, 2))
print("silsila" , round (r[3]*100, 2))


