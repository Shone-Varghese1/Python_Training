# try:
#     x=10/0
# except ZeroDivisionError:
#     print("ZeroDivisionError")

try:
    num = int(input("Enter a number: "))
    print(10/num)
except ValueError:
    print("invalid input")
except ZeroDivisionError:
    print("ZeroDivisionError")