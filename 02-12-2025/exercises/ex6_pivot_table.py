# F. PIVOT TABLES (5)
import pandas as pd
import numpy as np
df=pd.read_csv("Superstore.csv")
df["OrderDate"]=pd.to_datetime(df["OrderDate"])
df["ShipDate"]=pd.to_datetime(df["ShipDate"])
df_table=pd.pivot_table(df,index="Region",columns="Category",values="Sales",fill_value=0,aggfunc="sum")
print(df_table)
# Pivot showing Profit by SubCategory and Segment.
df_table2=pd.pivot_table(df,index="Segment",columns="SubCategory",values="Profit",fill_value=0,aggfunc="sum")
print(df_table2)
# Pivot showing count of orders by Returned status and Region.
df_table3=pd.pivot_table(df,index="Region",columns="Returned",values="OrderID",fill_value=0,aggfunc="count")
print(df_table3)
# Pivot showing average UnitPrice per Category.
df_table4=pd.pivot_table(df,columns="Category",values="UnitPrice",fill_value=0,aggfunc="mean")
print(df_table4)
# Pivot showing total Quantity per Month and Region.
df["Month"]=df["OrderDate"].dt.month

df_table5=pd.pivot_table(df,index="Region",columns="Month",values="Quantity",fill_value=0,aggfunc="sum")
print(df_table5)

