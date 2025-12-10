# 14. Write a function that checks if a given date is in the future, past, or today.
from datetime import date
date1=input("enter date seperated by - in d,m,yyyy :")
d,m,y=date1.split("-")
start_date= date (int(y),int(m),int(d))
if start_date > date.today():
    print("the date is in the future")
elif start_date < date.today():
    print("the date is in the past")
else:
    print("the date is today")


