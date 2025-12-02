# CLEANING & TRANSFORMATIONS (5)
#





# 6. Create a new column ShippingDays = ShipDate - OrderDate.
import pandas as pd
import numpy as np
df=pd.read_csv("Superstore.csv")
print(df.info())
df["OrderDate"]=pd.to_datetime(df["OrderDate"])
df["ShipDate"]=pd.to_datetime(df["ShipDate"])

df["ShippingDays"]=df["ShipDate"]-df["OrderDate"]
print(df.head())

# 7. Create ProfitMargin = Profit / Sales.

df["ProfitMargin"]=df["Profit"]/df["Sales"]
print(df.head())

# 8. Standardize CustomerName to title case.
df["CustomerName"] = df["CustomerName"].str.replace(" ", "", regex=False)
#split names based on capital letter
import re
df["CustomerName"] = df["CustomerName"].apply(
    lambda x: " ".join(re.findall(r'[A-Z][a-z]*', x))
)

df["CustomerName"]=df["CustomerName"].str.title()
print(df["CustomerName"])

# 9. Remove rows where Sales is zero or negative.
new_df=df[df["Sales"]>0]
print(new_df)
print(new_df["Sales"])
# 10. Convert Discount from decimal to percentage format.
new_df["Discount"] = new_df["Discount"]*100
print(new_df["Discount"])
