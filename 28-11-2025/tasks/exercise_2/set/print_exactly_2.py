# 11. Given a list, print only those elements whose frequency is exactly 2 using sets.

list1 = [1, 2, 3, 2, 4, 1, 5, 6,2,5, 1, 4]

seen_once = set()
seen_twice = set()
seen_more = set()

for item in list1:
    if item in seen_once:
        if item in seen_twice:
            seen_more.add(item)
        else:
            seen_twice.add(item)
    else:
        seen_once.add(item)

result = seen_twice - seen_more
print(result)
