
# 4. Find the top 5 highest-value orders by TotalPrice.
import pandas as pd
df = pd.read_csv("sales_data.csv")

sorted_df=df.sort_values(by="TotalPrice", ascending=False)
print(sorted_df.head(5))