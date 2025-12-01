# Build a safe list access function: if index is out of range, return a message instead of error.

list1=[10,20,30,40,50]
for i in range(0,len(list1)+1):
    try:
        print(list1[i])
    except IndexError:
        print("index out of range")

