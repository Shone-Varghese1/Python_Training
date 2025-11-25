words = ["apple", "banana", "grape"]
new_set=set()
for word in words:
    for char in word:
        new_set.add(char)
print(new_set)
