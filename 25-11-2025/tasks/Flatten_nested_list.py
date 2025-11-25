list1=[[1,2,3],[4,5],6,[7,8,9]]
new_list=[]
for i in range(0,len(list1)):
    if type(list1[i]) is int:
        new_list.append(list1[i])
    else:
        for j in range(0, len(list1[i])):
            new_list.append(list1[i][j])

print(new_list)

