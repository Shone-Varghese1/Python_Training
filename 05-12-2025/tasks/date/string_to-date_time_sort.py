# 19. Convert a list of date strings into datetime objects and sort them.


date_strings = [
    "2025-12-10",
    "2026-12-12",
    "2025-12-15",
    "2025-12-20",
    "2025-12-28",
    "2026-01-03",
    "2025-01-07",
    "2026-01-05",
    "2026-01-09",
    "2026-01-18",
    "2026-01-25",
    "2026-01-31"
]
from datetime import datetime,date,time,timedelta
new_list=[]
for v in date_strings:
    v = datetime.strptime(v, "%Y-%m-%d").date()
    new_list.append(v)
new_list.sort()

sorted_strings = [d.strftime("%Y-%m-%d") for d in new_list]
print(sorted_strings)


