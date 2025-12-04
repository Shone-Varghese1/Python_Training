s=(2,'shone','hello',5,7,"hi")
string_list=[]
num_list=[]
for i in s:
    if isinstance(i,str):
        string_list.append(i)
    elif isinstance(i,int):
        num_list.append(i)
    else:
        print("invalid input")
print(tuple(string_list))
print(tuple(num_list))

