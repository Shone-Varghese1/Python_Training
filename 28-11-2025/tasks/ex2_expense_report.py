# 2. Expense Report Generator
# Create a function that accepts multiple expense items (name, amount) and writes a formatted expense
# report into report.txt .
expense_dict={
    "Book":100,
    "Pen":25,
    "pencil":15,
    "Marker":200
}
def expense_report(dict1):
    total=0
    for key,value in dict1.items():
        total+=value
        str1=f" the {key}s cost {value} rupees "
        with open("./textfiles/expense_report.txt",'a') as f:
            f.write(f"{str1}\n")
    with open("./textfiles/expense_report.txt", 'a') as f:
        f.write(f"total amount : {total}\n")
expense_report(expense_dict)