# 15. Given a order date and expected delivery timeline (like 3 days), calculate estimated delivery
# date.
from datetime import date,timedelta
date1=input("enter order date separated by - in d,m,yyyy :")
d,m,y=date1.split("-")
start_date= date (int(y),int(m),int(d))
time_line=int(input("enter expected delivery timeline :"))

expected_delivery=start_date + timedelta(days=time_line)
print(expected_delivery)


