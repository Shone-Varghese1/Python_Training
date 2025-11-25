set_1={1,3,5}
set_2={2,4,6}
flag=True
for i in set_1:
    if i in set_2:
        flag=False
        break

if flag:
    print("disjoint")
else:
    print("not disjoint")
