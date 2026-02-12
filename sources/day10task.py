import pandas as pd
df = pd.read_csv("sample_orders.csv")
print(df.head())
print(df.isna().sum())
print(df.fillna(0))
print( df["quantity"].fillna(df["quantity"].median()))
df["quantity"] = df["quantity"].fillna(df["quantity"].median())
print(df.duplicated().sum())
print(df.drop_duplicates())

#Task 2 
print(df.dtypes)
df["price"]=df["price"].str.replace("$","", regex=False)
df["price"]=df["price"].astype(float)
print(df["price"].astype(float))
print(df["quantity"].astype(float))
df["date"] = pd.to_datetime(df["date"]) 
df.dtypes

#Task 3
df["order_id"].str.strip()
df["order_id"]=df["order_id"].str.upper()
df["product"]=df["product"].str.lower()
print(df["order_id"].unique().sum())
print(df["product"].unique().sum())

