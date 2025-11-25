#  Exercise 18 — Multiplication Table
# Ask the user for a number and print a 1–10 multiplication table

num=int(input("enter a number: "))
for i in range(1,11):
    print(f"{num} * {i}   =  { num*i}")