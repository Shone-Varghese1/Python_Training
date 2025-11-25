#  Exercise 13 — Convert Minutes to Hours & Minutes
#  Take total minutes as input.
#  Convert to hours + remaining minutes.

min=int(input("enter minutes value :"))
hrs=min//60
mins=min % 60
print(f"{hrs} hours and {mins} minutes")