# 5. Automated Welcome Letter Creator
#
# Write a function that takes a student's name and course, and generates a personalized welcome letter in
# a text file.


def welcome_letter():
    name1=input("Enter your name: ")
    course1=input("Enter your course: ")
    with open(f"./textfiles/{name1}_welcome_letter.txt","w") as f:
        f.write(f"Welcome to {course1} course \n {name1}\n")
welcome_letter()
