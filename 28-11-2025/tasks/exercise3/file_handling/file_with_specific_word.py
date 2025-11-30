with open("textfile_new/text2","r") as f:
    for line in f:
        data=line.split()
        if "python" in data:
            print(line.strip())
        else:
            continue