nums=[1,2,0,3,4,0,5,6,7,8,91,0,9]
i=0
for j in range(len(nums)):
    if nums[j]!=0:
        nums[i]=nums[j]
        i=i+1
for k in range(i,len(nums)):
    nums[k]=0
print(nums)