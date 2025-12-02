# 6. Add a new column Discount:
#
# 10 percent discount for Returning customers
# 5 percent discount for New customers
# Compute final price after discount.
import pandas as pd
df = pd.read_csv("sales_data.csv")
df["Discount"]=df["CustomerType"].apply(lambda x:5 if x=="New" else 10)
df["FinalPrice"] = df["TotalPrice"] - (df["Discount"] / 100) * df["TotalPrice"]
print(df.head(3))