
dict1 = {'a': 1, 'b': 2}
dict2 = {'b': 3, 'c': 4}

merged = {}


for key in set(dict1) | set(dict2):
    v1 = dict1.get(key)
    v2 = dict2.get(key)
    if v1 is not None and v2 is not None:
        merged[key] = [v1, v2]
    else:
        merged[key] = v1 if v1 is not None else v2

print(merged)