# 12. Contact Exporter
#
# Read a CSV file contacts.csv with name and phone columns.
# Generate a formatted text file contacts_export.txt listing:
# Name: Rahul | Phone: 9988776655
# Name: Aisha | Phone: 9123456789

import csv

with open("./textfiles/contacts.csv","r") as f:
    reader = csv.DictReader(f)
    for row in reader:
        with open(f"./textfiles/contacts_export.txt","a") as f:
            f.write(f"Name: {row['name']:<20}   | Phone: {row['phone']:15}\n")

