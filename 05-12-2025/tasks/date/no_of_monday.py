# 13. You are given a list of attendance timestamps. Count how many fall on a mon
# .
from datetime import datetime,date,time,timedelta

list1 = [
    "2025-12-01 09:15:00",  # mon

    "2025-12-02 10:30:00",  # tues
    "2025-12-03 11:45:00",  # Wednesday
    "2025-12-04 08:00:00",  # Thursday
    "2025-12-05 09:00:00",  # Friday
    "2025-12-08 09:20:00",  # mon

    "2025-12-09 10:10:00",  # tues
    "2025-12-15 09:05:00",  # mon

    "2025-12-16 14:00:00",  # tues
    "2025-12-22 09:00:00",  # mon

]

mondays=0
for li in list1:
    dt = datetime.strptime(li, "%Y-%m-%d %H:%M:%S")
    if dt.weekday() == 0:
        mondays=mondays+1
print(mondays)

