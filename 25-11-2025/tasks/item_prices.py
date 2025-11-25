dict_1={
    "apple":250,
    "orange":140,
    "banana":65,
    "mango":120,
    "pineapple":90
}
dict_1={k : v for k,v in dict_1.items() if v >100}
print(dict_1)
