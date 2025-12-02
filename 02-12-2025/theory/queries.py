import pandas as pd

df=pd.read_csv("retail.csv")



high_elec=df[(df["Category"]== "Electronics")& (df["TotalPrice"] > 10000)]
print(high_elec)

sorted_df=df.sort_values("TotalPrice",ascending=False)

category_sales=df.groupby("Category")["TotalPrice"].sum()
print(category_sales)

store_avg=df.groupby("Store")["TotalPrice"].mean()
print(store_avg)

city_orders=df.groupby("City")["OrderID"].count()
print(city_orders)