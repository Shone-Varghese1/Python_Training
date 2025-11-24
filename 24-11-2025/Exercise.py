#Exercise 1 — Simple Calculator
# Write a Python program that:
#  Asks the user for two numbers
#  Prints the sum, difference, product, and division

num1=int(input("enter num1: "))
num2=int(input("enter num2: "))

print("sum:",num1+num2)
print("Difference:",num1-num2)
print("Product :",num1*num2)
print("Division:",num1/num2)



#  Exercise 2 — Age in 2050
#  Write a program that:
#  Accepts the user’s birth year
#  Calculates their age in the year 2050

year=int(input("enter  your birth year:"))
diff=2050-year
print(f"you will {diff} year's old in 2050")

# Exercise 3 — Area of a Rectangle:
#  Write a program to calculate:
#  Area = length × width

length=int(input("Enter length: "))
breadth=int(input("Enter breadth: "))
print("area is : ",length*breadth)

#  Exercise 4 — Even or Odd
#  Write a Python program that:
#  Accepts a number
#  Prints whether it is even or odd

a=int(input("enter your number: "))
if a % 2==0:
    print(f"{a} is even")
else:
    print(f"{a} is odd")

# Exercise 5 — Simple Login Check
#  Write a program that asks:
#  username
#  password
#  If both match admin / 1234, print Login Successful, else print Invalid Login.

username=input("enter username :")
password =int(input("enter password :"))

if username=="admin" and password==1234:
    print("login Successful")
else:
    print("invalid Login")

# Exercise 12 — Square & Cube of a Number
#  Ask the user for a number.
#  Print its square and cube
a=int(input("enter a number :"))
print("Square :",a ** 2)
print("Cube :", a ** 3)

#  Exercise 13 — Convert Minutes to Hours & Minutes
#  Take total minutes as input.
#  Convert to hours + remaining minutes.

min=int(input("enter minutes value :"))
hrs=min//60
mins=min % 60
print(f"{hrs} hours and {mins} minutes")

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


#  Exercise 15 — Check Positive, Negative, or Zero
#  User enters a number.
#  Print:
#  Positive
#  Negative
#  Zero


num=int(input("enter a num"))
if num>0:
    print("positive")
elif num<0:
    print("negative")
else:
    print("Zero")

# Exercise 16 — Find the Last Digit of a
#  Number
#  Ask the user for any number.
#  Print the last digit.

num1=int(input('enter a num: '))
unit=num1 % 10
print("last digit is ",unit)

# Exercise 17 — Sum of First N Natural Numbers
#  Ask for N.
#  Use a loop to compute the sum
n=int(input("enter :"))
sum=0
for i in range(1,n+1):
    sum+=i
print("sum: ",sum)

#  Exercise 18 — Multiplication Table
# Ask the user for a number and print a 1–10 multiplication table

num=int(input("enter a number: "))
for i in range(1,11):
    print(f"{num} * {i}   =  { num*i}")

#Exercise 19 — Count Digits in a Number
num1=int(input("number :"))
num_str=str(num1)
print("total length",len(num_str))

#  Exercise 20 — Reverse a Number (Logic Basics)

num1=int(input("enter a number :"))
rev_num=0
while(num1>0):
    digit=num1%10
    rev_num=rev_num*10+digit
    num1=num1//10
print("reversed  number is ",rev_num)