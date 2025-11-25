#  Exercise 14 — Swap Two Variables
#  Ask for two numbers.
#  Swap them without using a third variable.

a=int(input("enter number 1: "))
b=int(input("enter Number 2: "))
print(f"before swap a : {a} , b is {b}")
a=a+b
b=a-b
a=a-b
print(f"after swap a : {a} , b is {b}")