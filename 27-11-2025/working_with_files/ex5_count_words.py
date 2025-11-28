with open("notes.txt", "r") as f:
    data = f.read()
    list1=data.split()
    print("no of words: ",len(list1))