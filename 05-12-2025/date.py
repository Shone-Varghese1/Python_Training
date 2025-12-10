from datetime import datetime,date,time,timedelta

today = date.today()
print(today)

print(today.year)
print(today.month)
print(today.day)

now=datetime.now()
print(now)

dob=date(1995,8,14)
print(dob)

now=datetime.now()
formatted=now.strftime("%y-%m-%d %H:%M:%S")
print(formatted)