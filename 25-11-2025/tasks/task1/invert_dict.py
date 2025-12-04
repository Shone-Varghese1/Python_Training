
original = {"a": 1, "b": 2, "c": 1}

inverted = {}

for key, value in original.items():
    if value in inverted:
        inverted[value].append(key)
    else:
        inverted[value] = [key]

print(inverted)
