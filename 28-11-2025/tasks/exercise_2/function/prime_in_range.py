def prime_in_range(a,b):
    prime_list=[]

    for i in range(a,b):
        flag = True
        for j in range(2,i):
            if i%j==0:
                flag=False
        if flag:
            prime_list.append(i)
    return prime_list
print(prime_in_range(2,10))