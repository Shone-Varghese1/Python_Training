try:
    with open("text.txt", "r") as f:
        print(f.read())
except FileNotFoundError:
    print("File not found error ")
except PermissionError:
    print("You don't have the necessary permissions.")
