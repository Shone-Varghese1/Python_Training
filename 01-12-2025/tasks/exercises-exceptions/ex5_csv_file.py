import csv
try:
    with open('test.csv') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader:
            print(row)
except FileNotFoundError:
    print("File not found")
except PermissionError:
    print("Permission denied")