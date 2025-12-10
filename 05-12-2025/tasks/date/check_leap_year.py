# 17. Write a function that returns True if a given year is a leap year.
def check_leap(year):

    return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)

y=int(input("enter year to check for leap"))
print("leap year" if check_leap(y) else "not leap year")
