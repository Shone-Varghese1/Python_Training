# G. JOINING / MERGING (4)

import pandas as pd
df=pd.read_csv("Superstore.csv")
# Create a discount lookup: Consumer=5, Corporate=8, Home Office=10 and merge it.
discount_segment=pd.DataFrame({
    "Segment":["Consumer","Corporate","Home Office"],
    "Discount":[5,8,10]
})
df=df.merge(discount_segment,on="Segment",how="left")
print(df[["Discount_y","Segment"]])
# Create a region tax table and merge.
region_tax=pd.DataFrame({
    "Region":["Central","West","East","South"],
    "Tax":[500,300,200,250]
})
df=df.merge(region_tax,on="Region",how="left")
print(df[["Discount_y","Segment","Region","Tax"]])
print()

# Merge customer-level totals into the main df.
customer_totals = df.groupby("CustomerName", as_index=False)[["Sales", "Profit"]].sum()
customer_totals.rename(columns={"Sales": "TotalSales", "Profit": "TotalProfit"}, inplace=True)
df = df.merge(customer_totals, on="CustomerName", how="left")
print(df.head())


# Merge product-level profitability summary.
product_profit = df.groupby("ProductName", as_index=False)["Profit"].sum()
product_profit.rename(columns={"Profit": "ProductTotalProfit"}, inplace=True)

df = df.merge(product_profit, on="ProductName", how="left")
print(df.head())


