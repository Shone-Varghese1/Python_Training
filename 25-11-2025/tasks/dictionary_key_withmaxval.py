marks={"A": 85, "B": 92, "C": 78, "D": 92}
max1=float('-inf')
key_max=[]
for key,value in marks.items():
    if value>max1:
        max1=value
        key_max=[key]
    elif value==max1:
        key_max.append(key)
print(key_max)


