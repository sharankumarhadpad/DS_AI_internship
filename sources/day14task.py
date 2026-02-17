import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.preprocessing import LabelEncoder
from sklearn.preprocessing import MinMaxScaler,StandardScaler
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures
from sklearn.metrics import r2_score
df = pd.read_csv("cars_ml_dataset.csv")
print(df.head())
df.info()
le = LabelEncoder()
df["encoded"]=le.fit_transform(df['Color'])
print(df["encoded"])
df = pd.get_dummies(df, columns=['Color'], drop_first=True)
df.head()                                                   


#task 2


standard_scaler = StandardScaler()
standardized_data = standard_scaler.fit_transform(df[["Age", "Salary"]])
df_standardized = pd.DataFrame(standardized_data, columns=["Age", "Salary"])
minmax_scaler = MinMaxScaler()
normalized_data = minmax_scaler.fit_transform(df[["Age", "Salary"]])

df_normalized = pd.DataFrame(normalized_data,columns=["Age", "Salary"])

plt.subplot(1,3,1)
plt.hist(df["Salary"])
plt.title("Salary Before Scaling")
plt.xlabel("Salary")
plt.ylabel("Frequency")



plt.subplot(1,3,2)
plt.hist(df_standardized["Salary"])
plt.title("After Standardization")
plt.xlabel("Standardized Salary")
plt.ylabel("Frequency")



plt.subplot(1,3,3)
plt.hist(df_normalized["Salary"])
plt.title("After Normalization")
plt.xlabel("Normalized Salary")
plt.ylabel("Frequency")
plt.tight_layout()
plt.show()

print("First 5 rows after Standardization:\n")
print(df_standardized.head())

print("\nFirst 5 rows after Normalization:\n")
print(df_normalized.head())

#task 3
X = df[["Age"]]
y = df["Price"]
linear_model = LinearRegression()
linear_model.fit(X, y)

y_pred_linear = linear_model.predict(X)
r2_linear = r2_score(y, y_pred_linear)
 
poly = PolynomialFeatures(degree=2)
X_poly = poly.fit_transform(X)

poly_model = LinearRegression()
poly_model.fit(X_poly, y)

y_pred_poly = poly_model.predict(X_poly)
r2_poly = r2_score(y, y_pred_poly)
print("R² Score (Linear Model):", round(r2_linear, 4))
print("R² Score (Polynomial Model):", round(r2_poly, 4))

if r2_poly > r2_linear:
    print("\nYes, the curved features improved the model!")
else:
    print("\nNo significant improvement.")
