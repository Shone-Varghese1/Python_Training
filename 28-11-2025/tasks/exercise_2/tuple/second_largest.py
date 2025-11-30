# 9. Given a tuple of numbers, find the second largest number.

tuple1=(120,75,55,65,82,80)
largest=second=float('-inf')
for tuples in tuple1:
    if tuples>largest:
        second=largest
        largest=tuples
    elif tuples>second:
        second=tuples
print(second)
