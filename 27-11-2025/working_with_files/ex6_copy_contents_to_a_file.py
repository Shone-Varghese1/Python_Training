with open("notes.txt","r") as f,open("output.txt","w") as g:
    for line in f:
        g.write(line)
with open("output.txt","r") as f:
    for line in f:
        print(line)