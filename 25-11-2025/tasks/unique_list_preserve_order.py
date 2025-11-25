list1=[3,2,2,1,6,7,6,8,9,1,8]
set1=set()
result=[]
for n in list1:
    if n not in set1:
        set1.add(n)
        result.append(n)
print(result)
