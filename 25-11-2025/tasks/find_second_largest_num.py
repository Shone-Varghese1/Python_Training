nums=[2,78,79,54,34,51,212]
max1,max2=0,0

for n in nums:
    if n>max1:
        max2=max1
        max1=n
    elif n>max2 and n!=max1:
        max2=n
print(max2)