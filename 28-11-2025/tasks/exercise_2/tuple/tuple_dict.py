# Tuples
# 8. Write a program to convert a list of tuples into a dictionary.


tuple1=[(1,2),(2,3),(3,4),(4,5),(5,6),(1,7)]
dict1={}
for tuples in tuple1:
    if tuples[0] not in dict1:
        dict1[tuples[0]]=tuples[1]
    else:
        if isinstance(dict1[tuples[0]],int):
            dict1[tuples[0]]=[dict1[tuples[0]],tuples[1]]
        else:
            dict1[tuples[0]].append(dict1[tuples[1]])
print(dict1)
