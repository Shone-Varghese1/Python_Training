#  Exercise 20 — Reverse a Number (Logic Basics)

num1=int(input("enter a number :"))
rev_num=0
while(num1>0):
    digit=num1%10
    rev_num=rev_num*10+digit
    num1=num1//10
print("reversed  number is ",rev_num)