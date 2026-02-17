#Task 1

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
df = pd.read_csv("housing.csv")
print(df.head())
sns.histplot(df['price'], kde=True)
plt.subplot(2,2,2)
sns.countplot(x='bedrooms',data=df)
df['price'].value_counts()
plt.show()


#Task 2

sns.scatterplot(x='price',y='area',data=df)
plt.subplot(2,2,2)
sns.boxplot(x='mainroad',y='parking',data=df)
plt.show()
print("/n as mainroad increases the Parking increases")


#task 3
corr_matrix = df.corr(numeric_only=True)
print(corr_matrix)
plt.figure(figsize=(6,4))
sns.boxplot(x=df["price"])
plt.title("Boxplot of Price")
plt.show()
