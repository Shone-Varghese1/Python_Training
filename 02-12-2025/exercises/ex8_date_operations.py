
from matplotlib import pyplot as plt
import pandas as pd
import numpy as np
df=pd.read_csv("Superstore.csv")
df["OrderDate"]=pd.to_datetime(df["OrderDate"])
df["ShipDate"]=pd.to_datetime(df["ShipDate"])
# Extract year, month, day from OrderDate.
df["Year"]=df["OrderDate"].dt.month # type: ignore
df["Month"]=df["OrderDate"].dt.month # type: ignore
df["Day"]=df["OrderDate"].dt.day # type: ignore
# Calculate which day of week each order was placed.
df["DayOfWeek"] = df["OrderDate"].dt.day_name()# type: ignore
print(df)
# Find orders shipped in more than 5 days.
df["ShippingDays"]=(df["ShipDate"]-df["OrderDate"]).dt.days
df_after_5=df[df["ShippingDays"]>5]
print(df_after_5)
# Group orders by month and compute sales.
print()
monthly_sales = df.groupby("Month")["Sales"].sum()
print(monthly_sales)



# Plot sales trend per month (line chart).
import matplotlib.pyplot as plt
monthly_sales.plot(kind="line", marker="o", title="Monthly Sales Trend")
plt.xlabel("Month")
plt.ylabel("Total Sales")
plt.grid(True)
plt.show()
