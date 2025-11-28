# Student Certificate Batch Generator
#
# Write a program that reads a list of student names from students.txt and generates a certificate
# file for each student automatically.


def certificate_generator(name):
    with open(f"./textfiles/{name}_certificate.txt", 'w') as f:
        str1=f"""
        {name} cleared the exam with distinction
        """
        f.write(str1)
def get_name():
    with open("student.txt", 'r') as f:
        for line in f:
            certificate_generator(line.strip())

get_name()