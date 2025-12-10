from datetime import datetime,date,timedelta,time

today=date.today()
next_week=today + timedelta(days=7)
print(next_week)
yesterday=today - timedelta(days=1)

print(yesterday)

start=date(2024,1,1)
end=date(2024,12,31)

diff=end-start
print(diff.days)
df=datetime.combine(date(2025,3,5), time(10,15))
print(df)