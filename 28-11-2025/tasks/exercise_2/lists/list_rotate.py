

# 6. Rotate a list to the right by N positions.
list1=[100,120,12,89,90,21]
num1=int(input("enter num to rotate"))
num1=num1 % len(list1)
for _ in range(num1):
    first=list1[-1]
    for i in range(len(list1)-1,0,-1):
        list1[i]=list1[i-1]
    list1[0]=first
print(list1)







