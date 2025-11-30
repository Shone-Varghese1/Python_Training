# Use lambda with filter to return only even numbers from a list.
list1=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
even_list=lambda list2:[l for l in list1 if l%2==0]
print(even_list(list1))


