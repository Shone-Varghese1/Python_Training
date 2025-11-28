with open("notes.txt", "r") as f:
    linecount=0
    for line in f:
        linecount=linecount+1
    print(linecount)
