


with open("./../textfiles/text",encoding="utf-8") as f:
    lines = f.readlines()


mid = len(lines) // 2


first_half = lines[:mid]
second_half = lines[mid:]

with open("./../textfiles/textfirst.txt","w", encoding="utf-8") as f1:
    f1.writelines(first_half)
with open("./../textfiles/textsecond.txt", "w", encoding="utf-8") as f2:
    f2.writelines(second_half)

print(f"File split successfully ")
