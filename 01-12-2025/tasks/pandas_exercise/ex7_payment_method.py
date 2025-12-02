# 7. Find how many orders were paid using:
# Cash
# Credit Card
# UPI

import pandas as pd

df = pd.read_csv("sales_data.csv")

count_upi=(df["PaymentMethod"]=="UPI").sum()
count_Credit_card=(df["PaymentMethod"]=="CreditCard").sum()
count_Credit_cash=(df["PaymentMethod"]=="Cash").sum()
print(count_upi)
print(count_Credit_card)
print(count_Credit_cash)