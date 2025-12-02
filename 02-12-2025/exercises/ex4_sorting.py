# D. SORTING (5)



import pandas as pd
import numpy as np
df=pd.read_csv("Superstore.csv")
df["OrderDate"]=pd.to_datetime(df["OrderDate"])
df["ShipDate"]=pd.to_datetime(df["ShipDate"])
print(df.info())

# 16. Sort by Sales descending.
sorted_df=df.sort_values("Sales",ascending=False)
print(sorted_df)
# 17. Sort by ProfitMargin.
print()

df["ProfitMargin"]=df["Profit"]/df["Sales"]

sorted_df2=df.sort_values("ProfitMargin",ascending=False)
print(sorted_df2)

# 18. Sort by Region then City.
sorted_df3 = df.sort_values(by=["Region", "City"])
print(sorted_df3)
print(sorted_df3[["Region","City"]])
# 19. Sort by ShippingDays largest to smallest.
sorted_df4=df.sort_values("ShipDate",ascending=False)
print(sorted_df4)

# 20. Sort by CustomerName alphabetical.

sorted_df5=df.sort_values("CustomerName")
print(sorted_df5["CustomerName"])