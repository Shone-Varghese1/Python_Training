# Exercise 17 — Sum of First N Natural Numbers
#  Ask for N.
#  Use a loop to compute the sum
n=int(input("enter :"))
sum=0
for i in range(1,n+1):
    sum+=i
print("sum: ",sum)