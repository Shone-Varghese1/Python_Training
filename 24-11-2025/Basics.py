#Basics.py

#Printing hello world

print("hello world")

#declaring variables

name="shone"
age=22
salary=8.5

print(name)
print(age)
print(salary)

#arithmetic operation
a=10
b=3

print("Addition",a+b)
print("division",a/b)
print("Multiplication",a * b)
print("Modulus",a % b)
print("power",a ** b)
print("int-divison",a//b)

#odd or even


nums=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]

for n in nums:
    if n % 2==0:
        print(f"{n} is even")
    else:
        print(f"{n} is odd")


#else if conditionals

marks=int(input("enter your marks: "))
if marks>=90:
    print("Grade A")
elif marks>=75:
    print("Grade B")
elif marks>=60:
    print("Grade C")
else:
    print("Grade D")

#for loops

for i in range(1,6):
    print("num :",i)

# while loops
    
count=1
 
while count <=5:
    print("count :",count)
    count+=1

# breaking out of a loop -break and continue
for i in range(10):
    if i==5:
        break
    print(i)
    
for i in range(10):
    if i % 2 ==0:
        continue
    print(i)