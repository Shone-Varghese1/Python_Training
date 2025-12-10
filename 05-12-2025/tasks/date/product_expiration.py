#Given a list of expiry dates, find which products expire within the next 15 days.
products_expiry = {
    "Milk": "2025-12-10",
    "Bread": "2025-12-15",
    "Cheese": "2025-12-20",
    "Butter": "2025-12-28",
    "Yogurt": "2026-01-03",
    "Juice": "2026-01-07",
    "Eggs": "2026-01-12",
    "Cereal": "2026-01-18",
    "Pasta": "2026-01-25",
    "Rice": "2026-01-31"
}
from datetime import datetime,date,time,timedelta
expired_items=[]
expiry_date=date.today()+timedelta(days=15)
for k,v in products_expiry.items():
    v = datetime.strptime(v, "%Y-%m-%d").date()

    if v<=expiry_date:
        expired_items.append(k)
print(expired_items)