# 7. Merge two lists into a dictionary of {key: value} where list1 is keys and list2 is values.
list1=[1,2,3,4,5]
list2=[10,20,30,40,50]
merge_dict={ list1[i]:list2[i]  for i in range(len(list1)) }
print(merge_dict)