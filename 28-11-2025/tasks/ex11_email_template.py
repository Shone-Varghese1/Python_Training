# 11. Email Template Generator
# Write a script that reads names from names.txt and generates email templates like:
#
# Dear <name>,
# Your training session starts tomorrow.
# Regards,
# Training Team
# Each email should be saved into separate files.
def email_writer(name):
    with open(f"./textfiles/{name}_email.txt","w") as f:
        str1=f"""Dear {name},
Your training session starts tomorrow.
Regards,
Training Team
"""
        f.write(str1)

with open("./textfiles/names.txt","r") as f:
    for line in f:
        email_writer(line.strip())

