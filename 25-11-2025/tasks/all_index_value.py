nums=[2,5,6,7,6,9,10,7,1,3,4,5,8]
index_list=[]
num=int(input("enter a number to check index :"))
i=0
for n in nums:
    if n==num:
        index_list.append(i)
    i+=1
print(index_list)