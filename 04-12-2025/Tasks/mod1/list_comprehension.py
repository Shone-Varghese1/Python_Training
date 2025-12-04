# 5. Read 10 values and store them into a list without using loops (use list comprehension).

values=[int(input(f"enter {i+1} element")) for i in range(10)]
print(values)
