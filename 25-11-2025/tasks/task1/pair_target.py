set1={2,4,6,8,10}
result=[]
target=12
for i in set1:
    for j in set1:
        if i+j==12 and i<=j:
            result.append((i,j))
print(result)
