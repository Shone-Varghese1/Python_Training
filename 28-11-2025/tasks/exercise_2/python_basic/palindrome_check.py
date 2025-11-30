# 2. Write a program to check if a given string is a palindrome.



str1=input("enter string to be checked for palindrome: ")
if str1==str1[::-1]:
    print("palindrome")
else:
    print("not palindrome")