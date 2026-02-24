import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("C:/Users/HP/Downloads/customer_analytics (1).csv")
print(df.head())
print(df.info())
print(df.describe())


#Phase 2

print(df.isnull().sum())
df = df.fillna(0)
print(df.isnull().sum())
print("\nNumber of duplicate rows:")
print(df.duplicated().sum())
df = df.drop_duplicates()
print("\nFinal cleaned dataset:")
print(df.head())

#Phase 3
plt.figure()
sns.histplot(df['Age'], kde=True)
plt.title("Age Distribution")
plt.show()

#The histogram shows that the majority of customers fall within the 20–40 age range.


plt.figure()
plt.hist(df['AnnualIncome'])
plt.title("Annual Income Distribution")
plt.show()

#The income distribution shows variation across customers, with most individuals concentrated in the mid-income range.

plt.figure()
sns.countplot(x='Gender', data=df)
plt.title("Gender Distribution")
plt.show()

#The gender distribution appears relatively balanced between male and female customers.

plt.figure()
sns.scatterplot(x='AnnualIncome', y='SpendingScore', data=df)
plt.title("Income vs Spending Score")
plt.show()

#The scatter plot shows that higher income does not necessarily correspond to higher spending scores.

plt.figure()
sns.scatterplot(x='Age', y='SpendingScore', data=df)
plt.title("Age vs Spending Score")
plt.show()

#The relationship between age and spending score appears weak, with spending distributed across different age groups.
