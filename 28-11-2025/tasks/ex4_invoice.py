# 4. Invoice Generator from CSV
#
# Read a CSV file orders.csv containing columns: item, quantity, price.
# Generate an invoice file that lists all items and the final total.
import csv

with open("./textfiles/orders_list.csv","r") as f:
    reader = csv.DictReader(f)
    for row in reader:
        with open(f"./textfiles/invoice.txt","a") as f:
            f.write(f"Item: {row['item']:<20}    Price: {int(row['quantity'])*int(row['price']):15}\n")