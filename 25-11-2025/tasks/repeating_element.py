nums=[1,2,3,1,2,4,5,6,7,2,10,8,7,9]
new_list=[]
for n in range(0,len(nums)):
    flag=False
    for j in range(n+1,len(nums)):
        if nums[n]==nums[j]:
            flag=True
            break
    if flag and nums[n] not in new_list:
        new_list.append(nums[n])
print(new_list)

