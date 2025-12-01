# Write
# a
# program
# using
# try–except– else –finally to read user input and write it into a file safely.

def write_to_file():
    try:
        f=open("text1.txt","w")
    except FileNotFoundError:
        print("file not exist")
    else:
        print("file exist")
        try:
            print("hello")
            f.write("hello world")
        except PermissionError:
            print("permission error")
        finally:
            try:
                f.close()
            except NameError:
                print("file was not opened")



write_to_file()