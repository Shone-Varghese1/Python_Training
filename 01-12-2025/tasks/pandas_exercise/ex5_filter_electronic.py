# 5. Filter the dataset to show only Electronics products with Quantity > 1.
import pandas as pd
df = pd.read_csv("sales_data.csv")
filtered = df[(df["Quantity"]>1) & (df["Category"]=="Electronics")]
print(filtered)