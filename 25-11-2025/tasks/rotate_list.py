num=int(input("enter number to rotate"))
list1=[10,20,30,40,50,60,70,80,90,100]
num=num % len(list1)
for _ in range(num):
    first=list1[0]
    for i in range(len(list1)-1):
        list1[i]=list1[i+1]
    list1[-1]=first
print(list1)
