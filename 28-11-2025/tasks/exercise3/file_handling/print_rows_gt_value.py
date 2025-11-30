import csv

with open("textfile_new/students.csv","r") as f:
    reader = csv.DictReader(f)
    for row in reader:
        if int(row["marks"])>85:
            print(f"Name : {row["name"]} Marks: {row["marks"]}")
