# 20. Generate a list of dates for the next 30 days starting from today.

from datetime import datetime,date,time,timedelta

today=date.today()
list1=[]
for i in range(1,31):
    newdate=today+timedelta(days=i)
    list1.append(newdate)
date_strings = [d.strftime("%Y-%m-%d") for d in list1]
print(date_strings)