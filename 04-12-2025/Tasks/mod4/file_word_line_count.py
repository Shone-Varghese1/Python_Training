line_count = 0
word_count = 0
char_count = 0

with open("./../textfiles/text","r") as f:

    for line in f.readlines():
        line_count+=1
        data=line.strip().split()
        word_count += len(data)
        for word in data:

            for ch in word:
                char_count+=1

print("line_count:",line_count)
print("word_count:",word_count)
print("char_count:",char_count)





