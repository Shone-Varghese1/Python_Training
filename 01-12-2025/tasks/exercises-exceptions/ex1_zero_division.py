# Write a program that takes two numbers as input and handles division by zero using try–except.
num1=int(input("Enter a number: "))
num2=int(input("Enter another number: "))
try:
    print(num1/num2)
except ZeroDivisionError:
    print("Division by zero error")
