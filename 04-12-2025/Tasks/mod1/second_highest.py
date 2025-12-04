# 4. Write a program that reads N numbers and returns the second highest value without sorting.

def second_last(nums):
    max1, max2 = 0, 0

    for n in nums:
        if n > max1:
            max2 = max1
            max1 = n
        elif n > max2 and n != max1:
            max2 = n
    return max2


n=int(input("enter no of elements in list"))
list1=[]
for i in range(n):
    num=int(input("enter elements"))
    list1.append(num)
print("second highest number is ",second_last(list1))


