import matplotlib.pyplot as plt
import pandas as pd

data = pd.read_csv("hpmarch2023.csv")
print(data)

x = data["area"]
y = data["price"]

plt.scatter(x,y)
plt.xlabel("Area")
plt.ylabel("price")
plt.title("Lonavala Bunglow")
plt.show()