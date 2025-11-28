with open("sample.txt","w") as f:
    f.write("hello world .\n")
    f.write("this file was created by python .\n")

with open("sample.txt","r") as f:
    content = f.read()
    print(content)