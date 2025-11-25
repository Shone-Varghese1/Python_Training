#  Exercise 4 — Even or Odd
#  Write a Python program that:
#  Accepts a number
#  Prints whether it is even or odd

a=int(input("enter your number: "))
if a % 2==0:
    print(f"{a} is even")
else:
    print(f"{a} is odd")