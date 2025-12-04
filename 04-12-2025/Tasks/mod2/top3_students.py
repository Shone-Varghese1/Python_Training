# 8. Given a dictionary of student marks, return the top 3 students.

marks={
    "stud1":75,
    "stud2":80,
    "stud3":90,
    "stud4":96,
    "stud5":67,
    "stud6":68,
    "stud7":99,
    "stud8":80,
    "stud9":41
}


top3=[k  for k, v in sorted(marks.items(), key=lambda x: x[1],reverse=True) [:3]]
print(top3)
