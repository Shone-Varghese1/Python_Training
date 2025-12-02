# E. GROUPBY ANALYSIS (6)

# 26. Mean ShippingDays grouped by Category.
import pandas as pd
import numpy as np
df=pd.read_csv("Superstore.csv")
df["OrderDate"]=pd.to_datetime(df["OrderDate"])
df["ShipDate"]=pd.to_datetime(df["ShipDate"])

# 21. Total Sales per Region.
Region_sales=df.groupby("Region")["Sales"].sum()
print(Region_sales)
print()
# 22. Average Profit per Category.
avg_profit_category=df.groupby("Category")["Profit"].mean()
print(avg_profit_category)
print()
# 23. Count of orders per Customer.
order_count_customer=df.groupby("CustomerName").size()
print(order_count_customer)
# 24. Sum of Sales per Segment.
print()
segment_sales=df.groupby("Segment")["Sales"].sum()
print(segment_sales)
# 25. Total Quantity sold per SubCategory.
print()
quantity_per_subcategory=df.groupby("SubCategory")["Quantity"].sum()
print(quantity_per_subcategory)
# 26. Mean ShippingDays grouped by Category.
df["ShippingDays"] = (df["ShipDate"] - df["OrderDate"]).dt.days
print()
mean_shipping_days=df.groupby("Category")["ShippingDays"].mean()
print(mean_shipping_days)
