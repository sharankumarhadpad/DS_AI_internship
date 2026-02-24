import pandas as pd
df = pd.read_csv("train.csv")
print(df.head())
print(df.info())
print(df.describe())

#task2

import pandas as pd
import matplotlib.pyplot as plt
print(df.isnull().sum())
filled = df.fillna(20)
print(filled.isnull().sum())
print("\nNumber of duplicate rows:")
print(df.duplicated().sum())
print("there is no duplicate rows present")
plt.subplot(1,3,1)
plt.hist(df["Age"])
plt.title("Age")

plt.subplot(1,3,2)
plt.hist("Passengers")
plt.title("Passengers")
plt.subplot(1,3,3)
plt.hist("Pclass")
plt.title("Pclass")
plt.tight_layout()
plt.show()

