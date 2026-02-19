import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
data = pd.read_csv("distribution_dataset.csv")
df = pd.DataFrame(data)
print(df)
print(df.head())
plt.subplot(1,3,1)
sns.histplot(data["Height_cm"], kde=True)
plt.subplot(1,3,2)

sns.histplot(data["Household_Income"], kde=True)
plt.subplot(1,3,3)
sns.histplot(data["Exam_Score"], kde=True)
plt.show()
print(data["Height_cm"].mean())
print(data["Height_cm"].median())
print("Mean = Median it's symmetric")

#task 2
mean = (data["Height_cm"].mean())
std =(data["Height_cm"].std())
data["z_score"] = (data["Height_cm"] - mean) / std
print(data["z_score"])
if (data["z_score"] > 3).any():
    print("All z_scores are more than 3")
else:
    print("z_scores are not more than 3")

#task2
import numpy as np
means = []

for _ in range(1000):
    sample = np.random.choice(data["Exam_Score"], size=30)
    means.append(sample.mean())

sns.histplot(means, bins=30, kde=True)
plt.title("Distribution of Sample Means")
plt.show()
