

# 1. Write a program to take three numbers as input and print the largest.
num1=int(input("enter First number: "))
num2=int(input("enter Second number: "))
num3=int(input("enter Third number: "))

if num1>num2 and num1>num3:
    print(num1," is largest")
elif num2>num3 and num2>num1:
    print(num2," is largest")
elif num3>num1 and num3>num2:
    print(num3," is largest")
else:
    print("largest can't be determined")

