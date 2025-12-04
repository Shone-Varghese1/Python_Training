# 3. Implement a mini calculator with add, subtract, multiply, and divide using functions.

def add(num1,num2):
    print(f"{num1} + {num2} = {num1+num2}")
def subtract(num1,num2):
    print(f"{num1} - {num2} = {num1-num2}")
def multiply(num1,num2):
    print(f"{num1} * {num2} = {num1*num2}")
def divide(num1,num2):
    try:
        print(f"{num1} / {num2} = {num1/num2}")
    except ZeroDivisionError:
        print("Division by zero")
def calculator():

    while True:
        print("#"*20)
        num1=int(input("Enter first number: "))
        num2=int(input("Enter second number: "))
        choice = int(input("Enter your choice: 1.addition 2.subtract 3.multiply 4.divide:5.exit "))
        if choice == 1:
            add(num1,num2)
        elif choice == 2:
            subtract(num1,num2)
        elif choice == 3:
            multiply(num1,num2)
        elif choice == 4:
            divide(num1,num2)
        elif choice == 5:
            break
        else:
            print("Please enter a valid choice")
calculator()

