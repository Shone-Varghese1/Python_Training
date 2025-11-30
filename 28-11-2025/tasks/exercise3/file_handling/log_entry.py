import datetime
timestamp=datetime.datetime.now()
with open("textfile_new/log.txt","a") as f:
    str1=f"{timestamp}\n"
    f.write(str1)