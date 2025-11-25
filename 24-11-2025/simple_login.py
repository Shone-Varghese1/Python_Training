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