def calculator():
    try:
        num1 = int(input("Enter first number: "))
        num2 = int(input("Enter second number: "))
    except ValueError:
        print("Invalid  provide new inputs")
        num1 = int(input("Enter first number: "))
        num2 = int(input("Enter second number: "))
    print("addition",num1+num2)
    print("subtraction",num1-num2)
    print("multiplication",num1*num2)
    try:
        print("division",num1/num2)
    except ZeroDivisionError:
        print("division by zero")
calculator()
