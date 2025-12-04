import csv
import json
data = []

with open("employees.csv", encoding='utf-8') as csv_file:
    csv_reader = csv.DictReader(csv_file)
    for row in csv_reader:
        data.append(row)
with open("./../textfiles/employee.json", 'w', encoding='utf-8') as json_file:
    json.dump(data, json_file, indent=4)