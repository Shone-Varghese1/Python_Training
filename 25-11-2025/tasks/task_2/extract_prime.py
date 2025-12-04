nums=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
prime=[]

for n in nums:
    flag=True
    if n==1:
        continue
    for i in range(2,n):
        if n%i==0:
            flag=False
    if flag:
        prime.append(n)
print(prime)