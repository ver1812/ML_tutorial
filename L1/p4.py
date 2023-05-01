#p4
import pandas as pd
data = pd.read_csv ("hpmarch2023.csv")
x = data ["area"]
y = data["price"]

r1 = 0
for i in range(len(x)):
  r1 = r1 + x[i]
print(r1)

r2 = 0
for i in range (len (y)):
  r2 = r2 + y[i]
print(r2)

r3 = 0
for i in range(len(x)):
  r3 = r3 + (x[i] * x[i])
print(r3)

r4 = 0
for i in range(len(y)):
  r4 = r4 + (y[i] * y[i])
print(r4)

r5 = 0
for i in range(len(x)):
  r5 = r5 + (x[i] * y[i])
print(r5)

b1 = ((5 * r5)-(r1*r2))/((5*r3)-(r1*r1))
b0 = (r2/5) - (b1 * r1/5)

print("b0 =",b0)
print("b1 = ",b1)

area= float(input("Enter area "))
price = b0 + b1 * area
print("price = ",price)



