t=(3,4,6,8,9)
flag=True
for n in range(len(t)-1):
    if t[n]>=t[n+1]:
        flag=False
        break

if flag:
    print("strictly increasing")
else:
    print("not strictly increasing")