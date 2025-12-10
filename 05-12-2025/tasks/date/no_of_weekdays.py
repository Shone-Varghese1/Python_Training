# 12. Given two dates (start_date, end_date), write a function that returns the number of weekdays.
from datetime import datetime,date,time,timedelta

start=date(2025,12,1)
end=date(2025,12,31)

current_date=start
weekday=0
while current_date<=end:
    if current_date.weekday()<5:
        weekday=weekday+1
    current_date=current_date+timedelta(days=1)
print(weekday)
