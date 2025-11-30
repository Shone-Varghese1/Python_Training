
# 5. Given a list of numbers, remove all duplicates without using set.
list1=[1,2,3,1,4,5,6,7,1,2,3]
seen={}
i=0
while i<len(list1):
    if list1[i] in seen:
        list1.pop(i)
    else:
        seen[list1[i]]=True
        i=i+1
print(list1)