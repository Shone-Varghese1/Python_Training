import pandas as pd

df=pd.read_csv("retail.csv")

print(df.info())
#describe for numeric data
print(df.describe())
print(df.isnull().sum())

df["Date"]=pd.to_datetime(df["Date"])
print(df.info())
df["Year"]=df["Date"].dt.year
df["Month"]=df["Date"].dt.month
df["Day"]=df["Date"].dt.day







print(df)