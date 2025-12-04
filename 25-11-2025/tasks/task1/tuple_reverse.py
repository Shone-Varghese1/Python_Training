names=("hello","shone","bye","world","malayalam")
reversed_list=[]
for n in names:
    reversed_list.append(n[::-1])
print(tuple(reversed_list))