# Sets
#
# 10. Given two sets, find elements that are in either set but not in both (without symmetric difference
# operator).



set1={1,2,3,7,8,9}
set2={4,5,6,7,8}

set3= set1 | set2
set4= set1 & set2
set5= set3 - set4
print(set5)