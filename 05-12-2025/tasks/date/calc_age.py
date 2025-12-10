

from datetime import datetime,date,time,timedelta


def calculate_age(birth_date):
    today = date.today()
    age = today.year - birth_date.year - ((today.month, today.day) < (birth_date.month, birth_date.day))
    return age


date1=input("enter birth date separated by - in d,m,yyyy :")
d,m,y=date1.split("-")
birth_date= date (int(y),int(m),int(d))
print(calculate_age(birth_date))