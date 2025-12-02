# 3. Calculate total sales (sum of TotalPrice) for each:
#
# Store
# City
# Category
import pandas as pd
df = pd.read_csv("sales_data.csv")
total_price_store=df.groupby("Store")["TotalPrice"].sum()
print(total_price_store)
total_price_category=df.groupby("Category")["TotalPrice"].sum()
print(total_price_category)
total_price_city=df.groupby("City")["TotalPrice"].sum()
print(total_price_city)
