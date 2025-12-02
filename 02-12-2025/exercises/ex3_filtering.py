# C. FILTERING (5)

import pandas as pd
import numpy as np
df=pd.read_csv("Superstore.csv")
df["OrderDate"]=pd.to_datetime(df["OrderDate"])
df["ShipDate"]=pd.to_datetime(df["ShipDate"])
print(df.info())
# 11. Filter all orders from the West region.
new_df= df[df["Region"]=="West"]
print(new_df.shape)
print(new_df["Region"])
# 12. Filter Technology category with Sales > 400.
filter_df=df[(df["Category"]=="Technology") & (df["Sales"]>400)]
print(filter_df.shape)
print(filter_df[["Category","Sales"]])
print("#################################################")
# 13. Find all products returned by customers.
products=df.loc[df["Returned"]=="Yes","ProductName"]
print(products)
# 14. Show Furniture orders shipped after 2024-01-20.
print("#################################################")
filter_df2=df[(df["Category"]=="Furniture") & (df["ShipDate"]>"2024-01-20")]
print(filter_df2.head())
print(filter_df2.shape)
# 15. Filter orders where Profit < 20.
print("#################################################")
filter_df3=df[df["Profit"]<20]
print(filter_df3.head())
print(filter_df3.shape)

