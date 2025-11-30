
people = [
    {"name": "Alice", "age": 30},
    {"name": "Bob", "age": 25},
    {"name": "Charlie", "age": 35}
]
sorted_person=sorted(people, key=lambda x: x["age"])
print(sorted_person)