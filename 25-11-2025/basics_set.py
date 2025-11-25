# # nums={10,20,30,40}
# # print(nums)
# # # no duplicates
# # data={1,2,3,3,2,4,5}
# # print(data)
# # #creating sets
# # set_1={1,2,3}
# # empty=set()
# # #add ops
# # s={1,2,3}
# # s.add(4)
# # print(s)
# # s.update([5,6])
# # print(s)
#
# #remove ops
# s.remove(3)# error if not found
# s.discard(10) # no error
# print(s)


# #union
# a={1,2,3}
# b={3,4,5}
# print(a | b)
# #intersection
# print(a & b)
# #difference
# print(a - b)
# #symmetric difference
# print(a ^ b)


s={10,20,30}
print(20 in s)

for item in {4,8,12}:
    print(item)
# if i want a unique list i can convert it into set and convert back to list
nums=[1,2,2,3,3,4]
unique=list(set(nums))
print(unique)