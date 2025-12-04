# 26. Write a program that appends log entries to a logfile with timestamps.

import datetime
timestamp=datetime.datetime.now()
with open("./../textfiles/log.txt","a") as f:
    str1=f"{timestamp}-Application started"
    f.write(str1)