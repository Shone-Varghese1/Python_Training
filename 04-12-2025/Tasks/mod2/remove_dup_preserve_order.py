# 6. Given a list of product prices, remove duplicates while maintaining order.


# 9. Flatten a nested list like [[1,2],[3,4],[5,6]] into a single list.


# 12. Given a tuple of names, return one tuple with unique names.
# 13. Build a program to reverse every alternate element in a list.
# 14. From a dictionary of employees, filter only employees with salary above 60000.
# 15. Given two dictionaries, combine them but sum values for matching keys.


list1=[3,2,2,1,6,7,6,8,9,1,8]
set1=set()
result=[]
for n in list1:
    if n not in set1:
        set1.add(n)
        result.append(n)
print(result)