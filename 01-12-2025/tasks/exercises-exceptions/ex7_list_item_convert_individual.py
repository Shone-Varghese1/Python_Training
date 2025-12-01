# Write a program that attempts to convert items of a list to integers, handling conversion errors individually.

list1=['10','20','30','40a','50']
for i in range (len(list1)):
    try:
        list1[i]=int(list1[i])
    except ValueError:
        print("Invalid input")
print(list1)



