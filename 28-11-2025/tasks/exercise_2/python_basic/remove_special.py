# 4. Write a program to remove all special characters from a string.

str1=input("enter string with special characters: ")

corrected_string="".join([char1 for char1 in str1 if char1.isalnum()]  )
print(corrected_string)