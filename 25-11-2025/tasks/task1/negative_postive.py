nums=[-2,-1,3,4,5,6,7,-1,-3,8]
pos_list=[]
neg_list=[]
for n in nums:
    if n>=0:
        pos_list.append(n)
    else:
        neg_list.append(n)
result=neg_list+pos_list
print(result)
