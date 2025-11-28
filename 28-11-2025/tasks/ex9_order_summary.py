# 9. Order Summary From User Input
# Ask the user for item name, quantity, and price for 3 items.
# Then generate a summary file order_summary.txt with totals.

for i in range(3):
    name1=input("Enter product name: ")
    quantity=int(input("Enter quantity purchases: "))
    price=int(input("Enter product price: "))

    with open("./textfiles/order_summary.txt","a") as f:
        str1= f"{name1}s total: {price*quantity}\n"
        f.write(str1)
