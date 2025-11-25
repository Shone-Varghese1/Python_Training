student={
    "Name":"Shone",
    "age": 22,
    "city": "kochi"
}
print(student["Name"])
print(student["age"])
print(student.get("city"))
student["mail"]="test@gmail.com"
student["city"]="alappuzha"

print(student)

# #removing values
# student.pop("age")
# del student["city"]
# print(student)
# student.clear()
# print(student)


for k in student.keys():
    print(k)
for k,v in student.items():
    print(k,v)
for v in student.values():
    print(v)