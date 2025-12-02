import pandas as pd
df = pd.read_csv("sales_data.csv")
df["Date"] = pd.to_datetime(df["Date"], format="%Y-%m-%d")


df["Year"] = df["Date"].dt.year
df["Month"] = df["Date"].dt.month
df["Day"] = df["Date"].dt.day

print(df.head(2))
