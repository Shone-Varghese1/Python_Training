tuple_1=(21,23,25,17,18,19,21,18)
index=[]
val=int(input("Enter a value in:21,23,18,19,21,25,17 for index: "))
for n in range(0,len(tuple_1)):
    if tuple_1[n]==val:
        index.append(n)
print(index)