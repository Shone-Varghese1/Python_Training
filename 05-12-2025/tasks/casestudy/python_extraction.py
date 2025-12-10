
# 6. Connect Python to MySQL and load the subscriptions table into a DataFrame.
import pymysql
import pandas as pd
from datetime import datetime, timedelta,date
import numpy as np
from datetime import date
conn = pymysql.connect(
#connection variables
)
df = pd.read_sql("SELECT * FROM subscriptions", conn)
conn.close()
print(df)

today=date.today()
# 7. Convert created_at into "DD-MM-YYYY HH:MM" format.
df["created_at"] = pd.to_datetime(df["created_at"], format="%Y-%m-%d %H:%M", errors="coerce")


# 8. Add a column days_overdue for expired subscriptions.



df["expiry_date"] = pd.to_datetime(df["expiry_date"], errors="coerce")

current_date = pd.Timestamp.today().normalize()


df["days_overdue"] = np.where(
    df["expiry_date"] < current_date,
    (current_date - df["expiry_date"]).dt.days,
    0
).astype(int)
# 9. Add a column next_billing_date .
df["next_billing_date"] = df["expiry_date"] + pd.Timedelta(days=1)

df["next_billing_date"] = pd.to_datetime(df["next_billing_date"], errors="coerce")

today = pd.Timestamp.today().normalize()

due_today_df = df[df["next_billing_date"] == today]

customers_due_today = due_today_df["customer_name"].tolist()
df["days_left"] = (df["expiry_date"] - today).dt.days
print(due_today_df)
print(customers_due_today)

# Generate a report showing active vs expired vs expiring soon.
def status(row):
    if row["days_left"] < 0:
        return "Expired"
    elif row["days_left"] <= 7:
        return "ExpiringSoon"
    else:
        return "Active"

df["status"] = df.apply(status, axis=1)
# Create a renewal reminder list containing customers whose days_left <= 5.
reminders = df.loc[
    df["days_left"].between(0, 5),  # includes today (0), excludes overdue (<0)
    ["sub_id", "customer_name", "expiry_date", "next_billing_date", "days_left", "plan_type"]
].copy()

print("\n(12) Renewal reminders (days_left <= 5):")
print(reminders)


# 13. Calculate customer lifetime (age_days).
df["age_days"] = (today - df["created_at"]).dt.days


# 14. Group by plan_type and calculate:
# total customers
# average age
# expected renewal revenue

price_map = {
"Monthly": 1000,
"Quarterly": 2700,
"Yearly": 10000
}
df["renewal_value"] = df["plan_type"].map(price_map)


df["next_billing_date"] = pd.to_datetime(df["next_billing_date"], errors="coerce")
today = pd.Timestamp.today()
window_end = today + pd.Timedelta(days=30)

df["expected_renewal_revenue"] = np.where(
    df["next_billing_date"].between(today, window_end),
    df["renewal_value"],
    0
)

plan_summary = df.groupby("plan_type").agg(
    total_customers=("sub_id", "count"),
    average_age_days=("age_days", "mean"),
    expected_renewal_revenue=("expected_renewal_revenue", "sum"),
).reset_index()

print(plan_summary)


# 15. Export the final DataFrame to subscription_report.csv .
print(df)
df.to_csv("output.csv", index=False)