


# 3. Write a program to count how many times each character appears in a string.
char_dict={}
str1=input("enter your string: ")
for char in str1:
    if char not in char_dict.keys():
        char_dict[char]=1
    else:
        char_dict[char]+=1
for key,value in char_dict.items():
    print(f" count of {key} character in {str1} is {value}")

