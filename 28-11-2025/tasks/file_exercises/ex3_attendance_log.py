# 3. Attendance Log Writer
# For each student name given by the user, append an entry to attendance.log with timestamp and
# status (Present/Absent).
import datetime
timestamp=datetime.datetime.now()
def attendance():
    while True:

        name1=input("enter student name")
        status=input("enter student status(absent/present)")
        with open("./textfiles/attendance_log.txt","a") as f:
            f.write(f"{name1}:{status} - {timestamp}\n")
        choice=int(input("press 1 to continue entering students \n press 2 to exit"))
        if choice==2:
            break
attendance()
