# Create a file that stores the squares of numbers from 1 to 20.
with open("textfile_new/numbers.txt","w") as f:
    for i in range (1,11):
        f.write(f"{i ** 2} \n")
