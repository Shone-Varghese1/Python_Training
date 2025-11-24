#lists.py

numbers=[10,20,30,40]
names=['shone','hari','ravi']
mixed=['hari',9,9.0,True]

print(numbers)
print(names)
print(mixed)
# accessing elements
fruits=['apple','banana','orange','cherry','blueberry']
print(fruits[0])
print(fruits[1])
print(fruits[-1])

#transforming list
fruits=['apple','banana','orange']
fruits[1]="grapes"

print(fruits)
fruits.append("mango")
print(fruits)
fruits.insert(1,'kiwi')
print(fruits)

#removing elements
fruits=['apple','banana','orange']
fruits.remove('banana')
fruits.pop(1)
fruits.pop()
del fruits[0]
print(fruits)