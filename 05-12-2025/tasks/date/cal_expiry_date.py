# 11. Given a customer’s subscription start date and duration (in days), compute expiry date.





from datetime import datetime,date,time,timedelta

date1=input("enter date seperated by - in d,m,yyyy :")
d,m,y=date1.split("-")
start_date= date (int(y),int(m),int(d))
duration=int(input("enter subscription duration in days"))
expiry_date=start_date + timedelta(days=duration)
print(expiry_date)